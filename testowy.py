
import mimetypes

if mimetypes.guess_type('/cygdrive/c/moje/aaa/git_nauka/nauka2/pliki_testowe_stat/test1.txt')[0] == 'text/plain':
    print 'True'
    # file is plaintext

# isBinary = os.system("file -b" + name + " | grep text > /dev/null")