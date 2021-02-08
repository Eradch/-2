
m_list = [(-1 + 0j), 1, 2.2, True, None, 'String', [3, 4],
          (5, 6, 6.5), {7: 'семь', 8: 'восемь'}, {9, 10},
          frozenset(), range(11), (b'twelve'), bytearray(b'thirteen'),
          zip(*[(14, 15),(16, 17), ('a', 'b')]), TypeError]
for i, item in enumerate(m_list, 1):
    print(f"{i}) {item} - {type(item)}")