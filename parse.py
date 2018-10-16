import re

text = r'                        Ethan E Dahlstrom                    </li></a>, <a href="index.php?q=%28%26%28cn%3Dethan%2A%29%28utexasEduPersonMajor%3D%2AComputer+Science%2C+Entry-Level%2A%29%29&amp;scope=student&amp;i=1"><li>                        Ethan L McWhirter                    </li></a>, <a href="index.php?q=%28%26%28cn%3Dethan%2A%29%28utexasEduPersonMajor%3D%2AComputer+Science%2C+Entry-Level%2A%29%29&amp;scope=student&amp;i=2"><li>                       Ethan Z Houston '
#r = re.compile()


def getNamesFromHTML(input_string):
    cleaned = cleanhtml(input_string)
    pieces = re.split(r"[\s]*,[\s]*", cleaned)
    print(pieces)

    final_pieces = []

    for i in pieces:
        final_pieces.append(i.strip())

    return final_pieces


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext


