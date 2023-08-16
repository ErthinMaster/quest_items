
import json, random

def load_file(filepath="ressource.json"): 
    with open(filepath, "r") as f:
        return json.load(f)

def write_file(data, filepath="result.txt"):
    with open(filepath, "w") as f:
        f.write("\n".join(data))

def _rec_generate_toc(ressources, toc=[], level=0, indexes=[], row_length=60, current_page=6, page_jump=[5,45]):    
    if not ressources: return current_page
    for key, sub_ressources in ressources.items():
        if level >= len(indexes): indexes.append(1)
        else: indexes[level] += 1
        line = f'{".".join([str(x) for x in indexes])} {key}'
        nb_dots = row_length - (len(line)+len(str(current_page)))
        toc.append(f'{line}{"."*nb_dots}{current_page}')        
        current_page = _rec_generate_toc(sub_ressources, toc, level+1, indexes, current_page=current_page+random.randint(page_jump[0],page_jump[1]))
    return current_page

if __name__ == '__main__':
    ressources = load_file()
    toc = []
    _rec_generate_toc(ressources, toc)
    write_file(toc)