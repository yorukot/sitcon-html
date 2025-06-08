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

## 📚 學習內容

### Chapter 1: HTML 基礎
- **1.html** - HTML 基本結構與 Hello World
- **2.html** - 文字格式化標籤（粗體、斜體、上下標、刪除線等）
- **3.html** - 表單元素與標籤關聯
- **example.txt** - 範例文字檔案
- **sitcon.png** - 圖片資源

**學習重點：**
- HTML 文件結構
- 常用文字格式化標籤
- 表單元素的使用
- 語義化標籤的重要性

### Chapter 2: CSS 樣式設計
- **1-font-family.html** - 字體設定與 Google Fonts
- **2-style-inheritance.html** - CSS 樣式繼承
- **3-other-css.html** - 其他 CSS 屬性
- **4-border-example.html** - 邊框樣式
- **5-bounding-box-example.html** - 盒模型
- **6-display-example.html** - 顯示屬性
- **7-flexbox-example.html** - Flexbox 佈局
- **hover-example.html** - 滑鼠懸停效果
- **width-height-example.html** - 寬高設定
- **style.css** - 共用樣式表

**學習重點：**
- CSS 基本語法與選擇器
- 盒模型概念
- Flexbox 佈局系統
- 響應式設計基礎
- 偽類選擇器

### Chapter 3: JavaScript 程式設計
- **1.html** - JavaScript 基礎語法與資料型別
- **2.html** - 進階 JavaScript 概念
- **3.html** - DOM 操作
- **4.html** - 事件處理
- **javascript.js** - 外部 JavaScript 檔案

**學習重點：**
- 變數宣告（const, let）
- 資料型別（Number, String, Boolean, Array, Object）
- 條件判斷與邏輯運算
- 函數定義與呼叫
- DOM 操作與事件處理

## 📝 作業練習

### Homework 目錄
包含 6 個漸進式的待辦事項練習：
- **todo-1.html** - 基礎 HTML 結構
- **todo-2.html** - 加入 CSS 樣式
- **todo-3.html** - 互動功能
- **todo-4.html** - 進階樣式
- **todo-5.html** - 響應式設計
- **todo-6.html** - 完整功能實作

**練習目標：**
- 整合 HTML、CSS、JavaScript 知識
- 建立實用的待辦事項應用
- 學習前端開發最佳實踐

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