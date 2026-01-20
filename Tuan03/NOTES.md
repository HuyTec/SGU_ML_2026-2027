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

