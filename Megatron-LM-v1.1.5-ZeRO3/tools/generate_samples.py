from essential_generators import DocumentGenerator
import random
import json


def generate_sample(paragraphs,line=100):
    fd = open('text.json', 'w')

    for i in range(line):
        fd.write('{')
        fd.write('"text"')
        fd.write(' : ')
        fd.write(str(random.choice(paragraphs)))
        fd.write('}')
        fd.write('\n')

    fd.close()
    return line



def main():
    gen = DocumentGenerator()
    paragraph_list = []
    sample_num = 10000
    for i in range(sample_num):
        paragraph_list.append(json.dumps(str(gen.paragraph())))

    generate_sample(paragraph_list, 10*len(paragraph_list))


if __name__ == "__main__":
    main()

