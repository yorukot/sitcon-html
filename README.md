
# 這個 README 是由 AI 產生的 可能有大量錯誤！！！

# SITCON HTML 學習專案

這是一個完整的前端開發學習專案，涵蓋了 HTML、CSS 和 JavaScript 的基礎知識，以及實際的專案練習。

## 📁 專案結構

```
sitcon-html/
├── chapter1/          # HTML 基礎
├── chapter2/          # CSS 樣式設計
├── chapter3/          # JavaScript 程式設計
├── homework/          # 作業練習
├── todo/              # 待辦事項 API 專案
├── .gitignore         # Git 忽略檔案設定
├── .editorconfig      # 編輯器設定
└── README.md          # 專案說明文件
```

## 🚀 Todo API 專案

### 技術棧
- **後端框架：** FastAPI (Python)
- **資料儲存：** JSON 檔案
- **API 功能：** RESTful API 設計

### 功能特色
- ✅ 新增待辦事項
- ✅ 查看所有待辦事項
- ✅ 更新待辦事項狀態
- ✅ 刪除待辦事項
- ✅ CORS 支援，可與前端整合

### 快速開始
```bash
cd todo
pip install -r requirements.txt  # 或使用 uv sync
python main.py
```

API 將在 `http://localhost:8000` 啟動

### API 端點
- `GET /todos` - 取得所有待辦事項
- `POST /todo` - 新增待辦事項
- `PUT /todo/{id}` - 更新待辦事項
- `DELETE /todo/{id}` - 刪除待辦事項

## 🛠️ 開發環境設定

### 編輯器設定
專案包含 `.editorconfig` 檔案，確保：
- UTF-8 編碼
- LF 行尾符號
- HTML/CSS/JS 使用 2 空格縮排
- Python 使用 4 空格縮排

### Git 設定
`.gitignore` 檔案已設定忽略：
- 資料庫檔案
- 系統生成檔案
- IDE 設定檔
- Node.js 相關檔案
- 日誌檔案
- 暫存檔案

## 🎯 學習建議

1. **循序漸進：** 按照 chapter1 → chapter2 → chapter3 的順序學習
2. **動手實作：** 每個範例都要親自執行和修改
3. **完成作業：** homework 目錄的練習有助於整合知識
4. **實際應用：** 嘗試修改和擴展 todo API 專案

## 📖 參考資源

- [MDN Web Docs](https://developer.mozilla.org/) - 權威的前端開發文件
- [W3Schools](https://www.w3schools.com/) - 適合初學者的教學資源
- [FastAPI 官方文件](https://fastapi.tiangolo.com/) - Python API 開發框架

## 🤝 貢獻

歡迎提交 Issue 或 Pull Request 來改善這個學習專案！

---

**Happy Coding! 🎉** 
