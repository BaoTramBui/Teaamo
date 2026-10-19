st.success("Gợi ý: **Hồng trà kem cheese** đậm vị trà giúp bạn tỉnh táo suốt buổi học!")
            elif "ngọt ngào" in mood:
                st.success("Gợi ý: **Trà sữa trân châu đường đen** ngọt ngào nạp lại năng lượng!")
            elif "Stress" in mood:
                st.success("Gợi ý: **Trà sữa thái xanh** thanh mát xua tan mọi căng thẳng!")
            else:
                st.success("Gợi ý: **Trà trái cây nhiệt đới** tươi tắn, sảng khoái!")
                
    with col_m2:
        st.subheader("🎋 Quẻ Bói Trà Sữa Hằng Ngày")
        if st.button("🎋 Rút Quẻ Ngay"):
            que_list = [
                ("Đại Cát (Đại吉)", "Hôm nay cực hợp uống Trà sữa thái xanh, tình duyên thăng hoa!"),
                ("Cát Tường", "Hồng trà kem cheese sẽ mang lại tài lộc và may mắn cả ngày!"),
                ("Bình An", "Một ly Trà trái cây nhiệt đới mang lại ngày mới nhẹ nhàng.")
            ]
            q, meaning = random.choice(que_list)
            st.warning(f"Quẻ của bạn: **{q}** — *{meaning}*")

with tab4:
    st.header("⭐ Tích Điểm Thành Viên & Đánh Giá")
    st.metric(label="Điểm tích lũy hiện tại của bạn", value=f"{st.session_state.points} Điểm")
    
    st.subheader("✍️ Đánh Giá Chất Lượng Dịch Vụ")
    review_text = st.text_area("Cảm nhận của bạn về hương vị và ứng dụng:")
    rating = st.slider("Chấm số sao:", 1, 5, 5)
    if st.button("Gửi Đánh Giá"):
        st.session_state.reviews.append({"text": review_text, "stars": rating})
        st.success("Cảm ơn bạn đã đánh giá! Phản hồi của bạn giúp quán ngày càng phát triển.")
        
    if st.session_state.reviews:
        st.markdown("### 💬 Đánh Giá Từ Khách Hàng Khác:")
        for r in st.session_state.reviews:
            st.write(f"- {'⭐' * r['stars']}: *{r['text']}*")
