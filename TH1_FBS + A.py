from queue import PriorityQueue

# Hàm tìm kiếm theo chiều rộng (BFS)
def duyetBFS(graph, batDau, dich):
    hangDoi = [batDau]
    daTham = {batDau: True}
    cha = {batDau: None}

    while hangDoi:
        hienTai = hangDoi.pop(0)

        if hienTai == dich:
            break

        for ke in graph.get(hienTai, []):
            if ke not in daTham:
                daTham[ke] = True
                hangDoi.append(ke)
                cha[ke] = hienTai

    duongDi = []
    hienTai = dich
    while hienTai is not None:
        duongDi.insert(0, hienTai)
        hienTai = cha[hienTai]
    return duongDi

# Hàm A* tìm đường tối ưu
def duyetAStar(graph, hamHeuristic, batDau, dich):
    hangDoiUuTien = PriorityQueue()
    hangDoiUuTien.put((0, batDau))
    chiPhi = {batDau: 0}
    cha = {batDau: None}

    while not hangDoiUuTien.empty():
        chiPhiHienTai, hienTai = hangDoiUuTien.get()

        if hienTai == dich:
            break

        for ke in graph.get(hienTai, []):
            # Kiểm tra nếu phần tử trong graph là một tuple có trọng số
            if isinstance(ke, tuple):
                ke, trongSo = ke
            else:
                trongSo = 1  # Nếu không có trọng số, mặc định là 1

            chiPhiMoi = chiPhi[hienTai] + trongSo
            if ke not in chiPhi or chiPhiMoi < chiPhi[ke]:
                chiPhi[ke] = chiPhiMoi
                uuTien = chiPhiMoi + hamHeuristic.get(ke, float('inf'))  # Dùng giá trị vô cùng nếu không có heuristic cho ke
                hangDoiUuTien.put((uuTien, ke))
                cha[ke] = hienTai

    duongDi = []
    hienTai = dich
    while hienTai is not None:
        duongDi.insert(0, hienTai)
        hienTai = cha[hienTai]
    return duongDi


# Dữ liệu đầu vào
graphBFS = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["f"],
    "d": ["g"],
    "e": ["g"],
    "f": ["g"],
    "g": []
}

graphAStar = {
    "a": [("b", 1), ("c", 2)],
    "b": [("d", 3), ("e", 1)],
    "c": [("f", 2)],
    "d": [("g", 4)],
    "e": [("g", 2)],
    "f": [("g", 1)],
    "g": []
}

hamHeuristic = {
    "a": 6, "b": 5, "c": 4,
    "d": 3, "e": 2, "f": 2,
    "g": 0
}

# Kết quả BFS
print("Duyệt BFS:")
duongDiBFS = duyetBFS(graphBFS, "a", "g")
print("Đường đi từ a đến g:", duongDiBFS)

# Kết quả A*
print("\nDuyệt A*: ")
duongDiAStar = duyetAStar(graphAStar, hamHeuristic, "a", "g")
print("Đường đi từ a đến g:", duongDiAStar)


# Bài kiểm tra 1
print("\nTest 1 - Duyệt BFS:")
graphTest1 = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": ["g"],
    "f": [],
    "g": []
}
duongDiTest1 = duyetBFS(graphTest1, "a", "g")
print("Đường đi từ a đến g:", duongDiTest1)

print("\nTest 1 - Duyệt A*: ")
duongDiTest1AStar = duyetAStar(graphTest1, hamHeuristic, "a", "g")
print("Đường đi từ a đến g:", duongDiTest1AStar)


# Bài kiểm tra 2
print("\nTest 2 - Duyệt BFS:")
graphTest2 = {
    "a": ["b", "c", "d"],
    "b": ["e"],
    "c": ["f"],
    "d": ["g"],
    "e": ["h"],
    "f": ["i"],
    "g": [],
    "h": [],
    "i": []
}
duongDiTest2 = duyetBFS(graphTest2, "a", "h")
print("Đường đi từ a đến h:", duongDiTest2)

print("\nTest 2 - Duyệt A*: ")
duongDiTest2AStar = duyetAStar(graphTest2, hamHeuristic, "a", "h")
print("Đường đi từ a đến h:", duongDiTest2AStar)


# Bài kiểm tra 3
print("\nTest 3 - Duyệt BFS:")
graphTest3 = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": ["g", "h"],
    "f": [],
    "g": [],
    "h": []
}
duongDiTest3 = duyetBFS(graphTest3, "a", "h")
print("Đường đi từ a đến h:", duongDiTest3)

print("\nTest 3 - Duyệt A*: ")
duongDiTest3AStar = duyetAStar(graphTest3, hamHeuristic, "a", "h")
print("Đường đi từ a đến h:", duongDiTest3AStar)


# Bài kiểm tra 4
print("\nTest 4 - Duyệt BFS:")
graphTest4 = {
    "a": ["b"],
    "b": ["c"],
    "c": ["d"],
    "d": ["e"],
    "e": ["f"],
    "f": ["g"],
    "g": []
}
duongDiTest4 = duyetBFS(graphTest4, "a", "g")
print("Đường đi từ a đến g:", duongDiTest4)

print("\nTest 4 - Duyệt A*: ")
duongDiTest4AStar = duyetAStar(graphTest4, hamHeuristic, "a", "g")
print("Đường đi từ a đến g:", duongDiTest4AStar)


# Bài kiểm tra 5
print("\nTest 5 - Duyệt BFS:")
graphTest5 = {
    "a": ["b", "c"],
    "b": ["d", "e"],
    "c": ["f"],
    "d": ["g"],
    "e": ["h"],
    "f": [],
    "g": [],
    "h": []
}
duongDiTest5 = duyetBFS(graphTest5, "a", "g")
print("Đường đi từ a đến g:", duongDiTest5)

print("\nTest 5 - Duyệt A*: ")
duongDiTest5AStar = duyetAStar(graphTest5, hamHeuristic, "a", "g")
print("Đường đi từ a đến g:", duongDiTest5AStar)



