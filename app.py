import streamlit as st

st.title("🧋 Teaamo - Milk Tea Ordering App")
st.write("Chào mừng bạn đến với ứng dụng đặt trà sữa của chúng tôi!")

# Menu trà sữa
menu = {
    "Trà sữa trân châu đường đen": 35000,
    "Trà sữa thái xanh": 30000,
    "Hồng trà kem cheese": 40000
}

selected_item = st.selectbox("Chọn món trà sữa:", list(menu.keys()))
quantity = st.number_input("Số lượng:", min_value=1, value=1)

if st.button("Đặt món ngay"):
    total = menu[selected_item] * quantity
    st.success(f"Bạn đã đặt thành công {quantity} phần {selected_item}! Tổng tiền: {total:,} VNĐ")