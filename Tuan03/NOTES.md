# Ghi chú

## Giải thuật tìm kiếm A* trên đồ thị (Source: Wikipedia)

```text
function A*(điểm_xuất_phát, đích)
    đóng := tập rỗng
    q := tạo_hàng_đợi(tạo_đường_đi(điểm_xuất_phát))

    while q không phải tập rỗng
        p := lấy_phần_tử_đầu_tiên(q)
        x := nút cuối cùng của p

        if x ∈ đóng
            continue

        if x = đích
            return p

        bổ sung x vào tập đóng

        foreach y in các_đường_đi_tiếp_theo(p)
            đưa_vào_hàng_đợi(q, y)

    return failure
```
### Ghi chú thêm (tuỳ chọn)
- `q` thường là **priority queue** sắp theo `f(n) = g(n) + h(n)`
- `đóng` chính là **closed set**
- `các_đường_đi_tiếp_theo(p)` là mở rộng nút cuối của đường đi `p`

### Layout thủ công cho cây với đầu vào là tập hợp {v , parent[v]}...
```
def hierarchy_pos(G, root, width=1., vert_gap=0.2, vert_loc=1, xcenter=0.5):
    pos = {}

    def _hierarchy_pos(G, root, left, right, vert_loc, pos):
        pos[root] = ((left + right) / 2, vert_loc)
        children = list(G.successors(root))
        if children:
            dx = (right - left) / len(children)
            nextx = left
            for child in children:
                nextx += dx
                pos = _hierarchy_pos(G, child, nextx - dx, nextx, vert_loc - vert_gap, pos)
        return pos

    return _hierarchy_pos(G, root, 0, width, vert_loc, pos)

```
## Tham khảo: 
### Thuật toán IDS (Iterative Deepening Search) và Best First Search 
### Uniform Cost Search = Dijkstra (thuật toán tối ưu đường đi dựa trên trọng số)
### Greedy Best First Search
### A* , IDA*

```
#
import matplotlib.pyplot as plt

n = len(state)

plt.figure(figsize=(4,4))

# Vẽ grid
for i in range(n+1):
    plt.plot([0,n], [i,i])
    plt.plot([i,i], [0,n])

# Vẽ số vào giữa ô
for i in range(n):
    for j in range(n):
        val = state[i][j]
        if val != 0:  # không vẽ ô trống
            plt.text(
                j + 0.5, n - i - 0.5,  # tọa độ giữa ô
                str(val),
                ha='center', va='center',
                fontsize=16
            )

plt.xlim(0,n)
plt.ylim(0,n)
plt.axis("off")
plt.show()
```