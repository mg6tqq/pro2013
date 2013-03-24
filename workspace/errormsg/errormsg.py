# hello worldを１文字変更した場合のエラーメッセージを調べる
# １文字削除、xを追加、1を追加
# python errormsg.py > output
# grep Hello.java output | sed 's/^.*: //' | sort | uniq

import sys
import subprocess

hello_src="""public class Hello {
    public static void main(String[] args) {
        System.out.println("hello, world");
    }
}
"""

def remove_one_char(str,index):
    return str[:index]+str[index+1:]

def insert_one_char(str,index,ch):
    return str[:index]+ch+str[index:]

def get_error_messages(filename, src):
    f = open(filename,"w")
    f.write(src)
    f.close()
    error = ""
    try:
#        subprocess.check_output(["javac","Hello.java"],stderr=subprocess.STDOUT)
        subprocess.check_output(["javac","-J-Duser.language=ja","-J-Dfile.encoding=utf8","Hello.java"],stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError, e:
        error = e.output
    return error;

def main():
    for i in range(len(hello_src)):
        print >> sys.stderr, i
        src = insert_one_char(hello_src,i,"x")
        error = get_error_messages("Hello.java", src)
        if error != "":
            print "========"
            print error
            print src

    for i in range(len(hello_src)):
        print >> sys.stderr, i
        src = insert_one_char(hello_src,i,"1")
        error = get_error_messages("Hello.java", src)
        if error != "":
            print "========"
            print error
            print src

    for i in range(len(hello_src)):
        print >> sys.stderr, i
        src = remove_one_char(hello_src,i)
        error = get_error_messages("Hello.java", src)
        if error != "":
            print "========"
            print error
            print src

main()

