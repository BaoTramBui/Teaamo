import streamlit as st

st.set_page_config(page_title="TeaMood - Milk Tea Ordering App", page_icon="🧋")

st.title("🧋 TeaMood - Milk Tea Ordering App")
st.write("Chào mừng bạn đến với ứng dụng đặt trà sữa sáng tạo của nhóm!")

# Menu sản phẩm
menu = {
    "Trà sữa trân châu đường đen": 35000,
    "Trà sữa thái xanh": 30000,
    "Hồng trà kem cheese": 40000,
    "Trà trái cây nhiệt đới": 38000
}

# Chọn món
selected_item = st.selectbox("Chọn món trà sữa:", list(menu.keys()))

# Tùy chỉnh đường đá và ghi chú
sugar = st.selectbox("Tùy chỉnh độ đường:", ["100% Đường", "70% Đường", "50% Đường", "0% Đường"])
ice = st.selectbox("Tùy chỉnh độ đá:", ["100% Đá", "50% Đá", "Không đá"])
quantity = st.number_input("Số lượng:", min_value=1, value=1)
note = st.text_input("Ghi chú cho quán:")

# Nút đặt món
if st.button("🚀 Xác Nhận Đặt Món"):
    total = menu[selected_item] * quantity
    st.success(f"Đặt thành công {quantity} phần {selected_item}!")
    st.info(f"Tổng tiền cần thanh toán: {total:,} VNĐ")
    
    # Hiển thị mã QR thanh toán mẫu
    st.write("Quét mã QR để thanh toán chuyển khoản:")
    st.image("https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=Payment_TeaMood", width=150)

# Các tính năng sáng tạo thêm
st.markdown("---")
st.subheader("🎁 Tiện ích vui nhộn")
if st.button("🎡 Quay Vòng Quay Nhận Voucher"):
    st.success("🎉 Chúc mừng! Bạn nhận được mã giảm giá 15% cho lần mua tiếp theo!")

if st.button("🎋 Rút Quẻ Bói Trà Sữa"):
    st.warning("🎋 Quẻ hôm nay: Đại Cát! Uống Hồng trà kem cheese để tình duyên thăng hoa!")
