# test_git
chi de test thui
1. đưa ổ chứa về máy mình: cd vô folder của mình rồi sử dụng "git clone http:duong_link_cua_git";
2. xem trong phạm vi ổ chứa có sửa cái gì không sử dụng "git status";
3. add những cái mình đã sửa "git add du_an_cua_ban";
4. đưa ổ chứa về vùng chứa cục bộ sử dụng "git commit -m "ly_do_ban_push";
5. sử dụng lại "git status để xem đã commit thành công hay chưa;
6. đẩy ổ chứa lên lại git sử dụng "git push origin main" "main" là nhánh bạn có thể chọn nhánh khác nếu có
---------------------------OKE VẬY LÀ XONG------------------------------
---------------------------CHAT GPT-------------------------------------
                TÓM TẮT CÁC BƯỚC CLONE & PUSH LÊN GITHUB
Bước 1: Cấu hình Git (nếu chưa)
    git config --global user.name "Tên GitHub của bạn"
    git config --global user.email "Email GitHub"
    git config --global credential.helper manager  # Lưu thông tin đăng nhập (Windows)
Bước 2: Clone repo từ GitHub
    Nếu dùng HTTPS (đơn giản):
        git clone https://github.com/<username>/<repo>.git
    Nếu dùng SSH (nên dùng lâu dài):
        git clone git@github.com:<username>/<repo>.git
Bước 3: Thêm hoặc sửa file trong thư mục repo
    cd <repo>
    # Thêm/sửa file ở đây
Bước 4: Commit các thay đổi
    git add .
    git commit -m "Thông điệp commit"
Bước 5: Push code lên GitHub
    git push origin main


