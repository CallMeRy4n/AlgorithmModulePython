dict_word = {"a":1,"b":2,"c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,"j":10,"k":11,"l":12,"m":13,"n":14,"o":15,"p":16,"q":17,"r":18,"s":19,"t":20,"u":21,"v":22,"w":23,"x":24,"y":25,"z":26}
#a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z total 26
def so_sanh(first: str, second: str):
    shortest_length = len(first) if len(first) < len(second) else len(second)

    for i in range(shortest_length):
        if dict_word.get(first[i]) > dict_word.get(second[i]):
            return second

        elif dict_word.get(first[i]) < dict_word.get(second[i]):
            return first
        
    # Else return shortest word
    return first if len(first) == shortest_length else second

def word_sort_by_char(array_list: list):
    orginal_length = len(array_list)
    new_list = []
    # Code start

    def convert(word: str):
        return [dict_word.get(char) for char in word]

    while len(new_list) < orginal_length:
        current_highest = ""

        for string in array_list:
            if string not in new_list:
                if current_highest == "":
                    current_highest = string
                else:
                    current_highest = so_sanh(current_highest, string)

        new_list.append(current_highest)
        del current_highest
    # Code end
    return new_list