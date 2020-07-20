dict_word = {"a":1,"b":2,"c":3,"d":4,"e":5, "f":6, "g":7, "h":8, "i":9, "j":10, "k":11 ,"l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19 ,"t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z":26}
#a	b	c	d	e	f	g	h	i	j	k	l	m	n	o	p	q	r	s	t	u	v	w	x	y	z total 26
def word_sort(array_list: list):
    new_list = []
    checked_list = []
    while len(new_list) is not len(array_list):
        current_highest = [None, ""]
        for string in array_list:
            total_sum = 0
            if string not in checked_list:
                for char in string:
                    total_sum = total_sum + dict_word.get(char, 0)# if not found then default is 0
                    
                if current_highest[0] is None or current_highest[0] > total_sum:
                    current_highest[0] = total_sum
                    current_highest[1] = string

        new_list.append(current_highest[1])
        checked_list.append(current_highest[1])
        del current_highest
    return new_list

# input_val = ["abe", "bre", "ber", "foo", "bar"]
# print(word_sort(input_val))
# Output: ['abe', 'bar', 'bre', 'ber', 'foo']