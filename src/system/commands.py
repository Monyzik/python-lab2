from enum import Enum


class Commands(str, Enum):
    cd = "cd"
    ls = "ls"
    cat = "cat"
    mv = "mv"
    cp = "cp"
    rm = "rm"
    zip = "zip"
    tar = "tar"
    unzip = "unzip"
    untar = "untar"
    grep = "grep"
    history = "history"
    undo = "undo"
