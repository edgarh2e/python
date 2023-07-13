import sys
from txt2speech import Txt2speech

sys.path.append('../python-nlsintacticcorrector')
from languagetoolnlsc import Correcttxt

args_txt = sys.argv[1]

txt = Correcttxt.correct(args_txt)
Txt2speech.speech(txt)

