import random
import data

pertanyaan = data.pertanyaan
index = data.index

while True:
    mat = data.mat
    print('------------------------------------------')
    print('Pikirkan 1 orang mahasiswa matematika 2017')
    print('Y = Ya')
    print('N = Tidak')
    print('Huruf lain = tidak tau')
    print('Tekan Enter jika sudah siap')
    input('------------------------------------------')

    shuffled_index = random.sample(index, len(index))
    for i in shuffled_index:
        #print(mat)
        #print()
        x = input(pertanyaan[i][0] + ' ')

        if x == 'Y' or x == 'y':
            mat = {k: v for k, v in mat.items() if pertanyaan[i][1] in v}
                
        elif x == 'N' or x == 'n':
            mat = {k: v for k, v in mat.items() if not pertanyaan[i][1] in v}

        if len(mat) == 1:
            print('Orang yang kamu pikirkan adalah : ' + list(mat.keys())[0])
            break
        elif len(mat) == 0:
            print('Mathkinator tidak bisa menebak siapa yang km pikirkan :(')
            break

    if len(mat) > 1:
        list_kemungkinan = list(mat.keys())
        str_kemungkinan = ', '.join(list_kemungkinan)
        print('Mathkinator belum bisa nentuin 1 :(')
        print('Tapi ada beberapa kemungkinan :)')
        print('Pasti ada di sini : ')
        print(str_kemungkinan)

    print()
    print('Ingin main lagi?')
    y =input()
    if not (y == 'y' or y == 'Y'):
        break
    else:
        print()