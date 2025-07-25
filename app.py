import streamlit as st

# Dữ liệu từ "Bảng phân vị tương quan" không thay đổi
conversion_table = [
    {"khoang": 1, "thpt_c": 15.00, "thpt_d": 17.00, "hoc_ba_a": 16.50, "hoc_ba_b": 19.80, "dgnl_a": 504, "dgnl_b": 595},
    {"khoang": 2, "thpt_c": 17.00, "thpt_d": 19.00, "hoc_ba_a": 19.80, "hoc_ba_b": 21.80, "dgnl_a": 595, "dgnl_b": 701},
    {"khoang": 3, "thpt_c": 19.00, "thpt_d": 22.60, "hoc_ba_a": 21.80, "hoc_ba_b": 25.50, "dgnl_a": 701, "dgnl_b": 872},
    {"khoang": 4, "thpt_c": 22.60, "thpt_d": 25.50, "hoc_ba_a": 25.50, "hoc_ba_b": 27.50, "dgnl_a": 872, "dgnl_b": 969},
    {"khoang": 5, "thpt_c": 25.50, "thpt_d": 28.50, "hoc_ba_a": 27.50, "hoc_ba_b": 28.50, "dgnl_a": 969, "dgnl_b": 1009},
    {"khoang": 6, "thpt_c": 28.50, "thpt_d": 30.00, "hoc_ba_a": 28.50, "hoc_ba_b": 30.00, "dgnl_a": 1009, "dgnl_b": 1200}
]

# Hàm quy đổi điểm không thay đổi
def quy_doi_diem(x, loai_diem):
    if loai_diem == "Học bạ":
        key_a, key_b = "hoc_ba_a", "hoc_ba_b"
    elif loai_diem == "ĐGNL":
        key_a, key_b = "dgnl_a", "dgnl_b"
    else:
        return None

    for row in conversion_table:
        a, b = row[key_a], row[key_b]
        if a < x <= b:
            c, d = row["thpt_c"], row["thpt_d"]
            y = c + ((x - a) / (b - a)) * (d - c)
            return y
    return None

# --- Giao diện ứng dụng web ---

# Tiêu đề của ứng dụng
st.title("Công cụ Quy đổi điểm ĐHQG-HCM")
st.write("Dựa trên Bảng phân vị tương quan mức điểm thi THPT, kết quả học tập THPT và điểm đánh giá năng lực.")

# Cho người dùng chọn loại điểm
loai_diem_chon = st.selectbox(
    "Chọn loại điểm bạn muốn quy đổi:",
    ("Học bạ", "ĐGNL")
)

# Dựa vào lựa chọn, hiển thị ô nhập điểm phù hợp
if loai_diem_chon == "Học bạ":
    diem_input = st.number_input(
        "Nhập điểm Kết quả học tập THPT (Học bạ) của bạn:",
        min_value=0.0, max_value=30.0, value=25.0, step=0.1, format="%.2f"
    )
else: # ĐGNL
    diem_input = st.number_input(
        "Nhập điểm thi Đánh giá năng lực (ĐGNL) của bạn:",
        min_value=0, max_value=1200, value=800, step=1
    )

# Nút để thực hiện tính toán
if st.button("Quy đổi điểm"):
    diem_quy_doi = quy_doi_diem(diem_input, loai_diem_chon)
    
    if diem_quy_doi is not None:
        st.success(f"Điểm {loai_diem_chon} '{diem_input}' của bạn tương đương với điểm thi THPT là: **{diem_quy_doi:.2f}**")
    else:
        st.error(f"Lỗi: Điểm '{diem_input}' nằm ngoài khoảng quy đổi được xác định trong bảng.")

# Hiển thị bảng tham chiếu
st.write("---")
st.subheader("Bảng tham chiếu")
st.image("https://i.imgur.com/2024-05-23-09-11-23.png") # Thay bằng link ảnh của bạn nếu muốn
