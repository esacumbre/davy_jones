import string
alphabet = list(string.ascii_lowercase)

def caesar_cypher(rot, input, encrypt=True):
    output = []
    for char in input:
        try:
            index = alphabet.index(char)
            index_rot_offset = index + rot if encrypt else index - rot
            
            if index_rot_offset < 0:
                26 + index_rot_offset
            elif index_rot_offset > 25:
                25 - index_rot_offset
            output.append(alphabet[index_rot_offset])
        except ValueError:
            output.append(char)

    return "".join(output)

first_clue = "uvag: qnil wbarf pbzznaqf gur frnf, n ornfg vafvqr urnqf uvf qrperrf. jura vg'f eryrnfrq, gur qhgpuzna fvatf. pbzznaq guvf ornfg yvxr n xvat naq guvf cneg lbh funyy jva."

for i in range(0, 25):
    rot_string = caesar_cypher(rot=i, input=first_clue, encrypt=False)
    print("rot: {} string: {}".format(i, rot_string))
