#!/usr/bin/env python

from __future__ import print_function

import sys
import os
import time

import amr
import smatch


ERROR_LOG = sys.stderr

DEBUG_LOG = sys.stderr

verbose = False

# directory on isi machine
# change if needed
isi_dir_pre = "/nfs/web/isi.edu/cgi-bin/div3/mt/save-amr"


def get_names(file_dir, files):
    """
    Get the annotator name list based on a list of files
    Args:
    file_dir: AMR file folder
    files: a list of AMR names, e.g. nw_wsj_0001_1

    Returns:
   a list of user names who annotate all the files
    """
    # for each user, check if they have files available
    # return user name list
    total_list = []
    name_list = []
    get_sub = False
    for path, subdir, dir_files in os.walk(file_dir):
        if not get_sub:
            total_list = subdir[:]
            get_sub = True
        else:
            break
    for user in total_list:
        has_file = True
        for f in files:
            file_path = file_dir + user + "/" + f + ".txt"
            if not os.path.exists(file_path):
                has_file = False
                break
        if has_file:
            name_list.append(user)
    if len(name_list) == 0:
        print("********Error: Cannot find any user who completes the files*************", file=ERROR_LOG)
    return name_list


def compute_files(user1, user2, file_list, dir_pre, start_num):

    """
    Compute the smatch scores for a file list between two users
    Args:
    user1: user 1 name
    user2: user 2 name
    file_list: file list
    dir_pre: the file location prefix
    start_num: the number of restarts in smatch
    Returns:
    smatch f score.

    """
    match_total = 0
    test_total = 0
    gold_total = 0
    for fi in file_list:
        file1 = dir_pre + user1 + "/" + fi + ".txt"
        file2 = dir_pre + user2 + "/" + fi + ".txt"
        if not os.path.exists(file1):
            print("*********Error: ", file1, "does not exist*********", file=ERROR_LOG)
            return -1.00
        if not os.path.exists(file2):
            print("*********Error: ", file2, "does not exist*********", file=ERROR_LOG)
            return -1.00
        try:
            file1_h = open(file1, "r")
            file2_h = open(file2, "r")
        except IOError:
            print("Cannot open the files", file1, file2, file=ERROR_LOG)
            break
        cur_amr1 = amr.AMR.get_amr_line(file1_h)
        cur_amr2 = amr.AMR.get_amr_line(file2_h)
        if cur_amr1 == "":
            print("AMR 1 is empty", file=ERROR_LOG)
            continue
        if cur_amr2 == "":
            print("AMR 2 is empty", file=ERROR_LOG)
            continue
        amr1 = amr.AMR.parse_AMR_line(cur_amr1)
        amr2 = amr.AMR.parse_AMR_line(cur_amr2)
        test_label = "a"
        gold_label = "b"
        amr1.rename_node(test_label)
        amr2.rename_node(gold_label)
        (test_inst, test_rel1, test_rel2) = amr1.get_triples()
        (gold_inst, gold_rel1, gold_rel2) = amr2.get_triples()
        if verbose:
            print("Instance triples of file 1:", len(test_inst), file=DEBUG_LOG)
            print(test_inst, file=DEBUG_LOG)
            print("Attribute triples of file 1:", len(test_rel1), file=DEBUG_LOG)
            print(test_rel1, file=DEBUG_LOG)
            print("Relation triples of file 1:", len(test_rel2), file=DEBUG_LOG)
            print(test_rel2, file=DEBUG_LOG)
            print("Instance triples of file 2:", len(gold_inst), file=DEBUG_LOG)
            print(gold_inst, file=DEBUG_LOG)
            print("Attribute triples of file 2:", len(gold_rel1), file=DEBUG_LOG)
            print(gold_rel1, file=DEBUG_LOG)
            print("Relation triples of file 2:", len(gold_rel2), file=DEBUG_LOG)
            print(gold_rel2, file=DEBUG_LOG)
        (best_match, best_match_num) = smatch.get_best_match(test_inst, test_rel1, test_rel2,
                                                             gold_inst, gold_rel1, gold_rel2,
                                                             test_label, gold_label)
        if verbose:
            print("best match number", best_match_num, file=DEBUG_LOG)
            print("Best Match:", smatch.print_alignment(best_match, test_inst, gold_inst), file=DEBUG_LOG)
        match_total += best_match_num
        test_total += (len(test_inst) + len(test_rel1) + len(test_rel2))
        gold_total += (len(gold_inst) + len(gold_rel1) + len(gold_rel2))
        smatch.match_triple_dict.clear()
    (precision, recall, f_score) = smatch.compute_f(match_total, test_total, gold_total)
    return "%.2f" % f_score


def get_max_width(table, index):
    return max([len(str(row[index])) for row in table])


def pprint_table(table):
    """
    Print a table in pretty format

    """
    col_paddings = []
    for i in range(len(table[0])):
        col_paddings.append(get_max_width(table,i))
    for row in table:
        print(row[0].ljust(col_paddings[0] + 1), end="")
        for i in range(1, len(row)):
            col = str(row[i]).rjust(col_paddings[i]+2)
            print(col, end='')
        print("\n")


def build_arg_parser():
    """
    Build an argument parser using argparse. Use it when python version is 2.7 or later.

    """
    parser = argparse.ArgumentParser(description="Smatch table calculator -- arguments")
    parser.add_argument("--fl", type=argparse.FileType('r'), help='AMR ID list file')
    parser.add_argument('-f', nargs='+', help='AMR IDs (at least one)')
    parser.add_argument("-p", nargs='*', help="User list (can be none)")
    parser.add_argument("--fd", default=isi_dir_pre, help="AMR File directory. Default=location on isi machine")
    parser.add_argument('-r', type=int, default=4, help='Restart number (Default:4)')
    parser.add_argument('-v', action='store_true', help='Verbose output (Default:False)')
    return parser


def cb(option, value, parser):
    """
    Callback function to handle variable number of arguments in optparse

    """
    arguments = [value]
    for arg in parser.rargs:
        if arg[0] != "-":
            arguments.append(arg)
        else:
            del parser.rargs[:len(arguments)]
            break
    if getattr(parser.values, option.dest):
        arguments.extend(getattr(parser.values, option.dest))
    setattr(parser.values, option.dest, arguments)


def check_args(args):
    """
    Parse arguments and check if the arguments are valid

    """
    if not os.path.exists(args.fd):
        print("Not a valid path", args.fd, file=ERROR_LOG)
        return [], [], False
    if args.fl is not None:
        # we already ensure the file can be opened and opened the file
        file_line = args.fl.readline()
        amr_ids = file_line.strip().split()
    elif args.f is None:
        print("No AMR ID was given", file=ERROR_LOG)
        return [], [], False
    else:
        amr_ids = args.f
    names = []
    check_name = True
    if args.p is None:
        names = get_names(args.fd, amr_ids)
        # no need to check names
        check_name = False
        if len(names) == 0:
            print("Cannot find any user who tagged these AMR", file=ERROR_LOG)
            return [], [], False
    else:
        names = args.p
    if len(names) == 0:
        print("No user was given", file=ERROR_LOG)
        return [], [], False
    if len(names) == 1:
        print("Only one user is given. Smatch calculation requires at least two users.", file=ERROR_LOG)
        return [], [], False
    if "consensus" in names:
        con_index = names.index("consensus")
        names.pop(con_index)
        names.append("consensus")
    # check if all the AMR_id and user combinations are valid
    if check_name:
        pop_name = []
        for i, name in enumerate(names):
            for amr in amr_ids:
                amr_path = args.fd + name + "/" + amr + ".txt"
                if not os.path.exists(amr_path):
                    print("User", name, "fails to tag AMR", amr, file=ERROR_LOG)
                    pop_name.append(i)
                    break
        if len(pop_name) != 0:
            pop_num = 0
            for p in pop_name:
                print("Deleting user", names[p - pop_num], "from the name list", file=ERROR_LOG)
                names.pop(p - pop_num)
                pop_num += 1
        if len(names) < 2:
            print("Not enough users to evaluate. Smatch requires >2 users who tag all the AMRs", file=ERROR_LOG)
            return "", "", False
    return amr_ids, names, True


def main(arguments):
    global verbose
    (ids, names, result) = check_args(arguments)
    if arguments.v:
        verbose = True
    if not result:
        return 0
    acc_time = 0
    len_name = len(names)
    table = []
    for i in range(0, len_name + 1):
        table.append([])
    table[0].append("")
    for i in range(0, len_name):
        table[0].append(names[i])
    for i in range(0, len_name):
        table[i+1].append(names[i])
        for j in range(0, len_name):
            if i != j:
                start = time.time()
                table[i+1].append(compute_files(names[i], names[j], ids, args.fd, args.r))
                end = time.time()
                if table[i+1][-1] != -1.0:
                    acc_time += end-start
            else:
                table[i+1].append("")
    # check table
    for i in range(0, len_name + 1):
        for j in range(0, len_name + 1):
            if i != j:
                if table[i][j] != table[j][i]:
                    if table[i][j] > table[j][i]:
                        table[j][i] = table[i][j]
                    else:
                        table[i][j] = table[j][i]
    pprint_table(table)
    return acc_time


if __name__ == "__main__":
    whole_start = time.time()
    parser = None
    args = None
    import argparse
    parser = build_arg_parser()
    args = parser.parse_args()
    # Regularize fd, add "/" at the end if needed
    if args.fd[-1] != "/":
        args.fd += "/"
    # acc_time is the smatch calculation time
    acc_time = main(args)
    whole_end = time.time()
    # time of the whole running process
    whole_time = whole_end - whole_start
    # print if needed
    # print("Accumulated computation time", acc_time, file=ERROR_LOG)
    # print("Total time", whole_time, file=ERROR_LOG)
    # print("Percentage", float(acc_time)/float(whole_time), file=ERROR_LOG)

