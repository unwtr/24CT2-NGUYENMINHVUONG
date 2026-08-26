import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Smart Parking - Chào bạn 24CT2 đến với học phần CNPM",
    page_icon="🚗",
    layout="wide",
)

# ---------- CSS ----------
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;   
        max-width: 1400px;
    }

    .brand {
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 0.1rem;
    }

    .subtitle {
        color: #6b7280;
        margin-bottom: 1.5rem;
    }

    .metric-card {
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 18px;
        background: white;
        min-height: 120px;
    }

    .metric-label {
        color: #6b7280;
        font-size: 0.9rem;
    }

    .metric-value {
        font-size: 2rem;
        font-weight: 800;
        margin-top: 8px;
    }

    .section-title {
        font-size: 1.2rem;
        font-weight: 750;
        margin: 1.5rem 0 0.8rem 0;
    }

    .slot {
        border-radius: 10px;
        padding: 14px 8px;
        text-align: center;
        border: 1px solid #e5e7eb;
        margin-bottom: 8px;
        font-weight: 700;
    }

    .available {
        background: #ecfdf5;
        color: #047857;
    }

    .occupied {
        background: #fef2f2;
        color: #b91c1c;
    }

    .camera-box {
        border: 2px dashed #d1d5db;
        border-radius: 14px;
        min-height: 330px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: #f9fafb;
        color: #6b7280;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ---------- Header ----------
st.markdown('<div class="brand">🚗 SMART PARKING - Chào bạn 24CT2 đến với học phần CNPM</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Hệ thống quản lý bãi đỗ xe thông minh bằng AI</div>',
    unsafe_allow_html=True,
)

# ---------- Metrics ----------
total = 20
occupied = 7
available = total - occupied

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Tổng số chỗ</div>'
        f'<div class="metric-value">{total}</div></div>',
        unsafe_allow_html=True,
    )

with c2:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Đang sử dụng</div>'
        f'<div class="metric-value">{occupied}</div></div>',
        unsafe_allow_html=True,
    )

with c3:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Còn trống</div>'
        f'<div class="metric-value">{available}</div></div>',
        unsafe_allow_html=True,
    )

with c4:
    st.markdown(
        f'<div class="metric-card"><div class="metric-label">Cập nhật</div>'
        f'<div class="metric-value">{datetime.now().strftime("%H:%M")}</div></div>',
        unsafe_allow_html=True,
    )

# ---------- Main ----------
left, right = st.columns([1.55, 1])

with left:
    st.markdown('<div class="section-title">📹 Camera giám sát</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="camera-box">
        <div>
            <div style="font-size:3rem;">📷</div>
            <div style="font-size:1.1rem;font-weight:700;">Camera chưa kết nối</div>
            <div style="margin-top:6px;">Sau này khung này sẽ hiển thị camera + bounding box YOLO.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-title">🚘 Nhận diện phương tiện</div>', unsafe_allow_html=True)

    data = [
        ["43A-123.45", "Ô tô", "14:32", "Đang đỗ"],
        ["43B-456.78", "Xe máy", "14:41", "Đang đỗ"],
        ["43C-789.12", "Ô tô", "14:48", "Đang đỗ"],
        ["43A-555.66", "Ô tô", "15:02", "Đã ra"],
    ]

    st.dataframe(
        data,
        column_config={
            0: "Biển số",
            1: "Loại xe",
            2: "Thời gian",
            3: "Trạng thái",
        },
        hide_index=True,
        use_container_width=True,
    )

with right:
    st.markdown('<div class="section-title">🅿️ Sơ đồ bãi đỗ</div>', unsafe_allow_html=True)

    slots = [
        ("A01", False), ("A02", True), ("A03", False), ("A04", True),
        ("A05", False), ("A06", True), ("A07", False), ("A08", False),
        ("B01", True), ("B02", False), ("B03", True), ("B04", False),
        ("B05", False), ("B06", False), ("B07", True), ("B08", False),
        ("C01", False), ("C02", False), ("C03", True), ("C04", False),
    ]

    cols = st.columns(4)
    for i, (name, is_occupied) in enumerate(slots):
        with cols[i % 4]:
            cls = "occupied" if is_occupied else "available"
            status = "Đang đỗ" if is_occupied else "Trống"
            st.markdown(
                f'<div class="slot {cls}">{name}<br>'
                f'<small>{status}</small></div>',
                unsafe_allow_html=True,
            )

    st.markdown("🟢 Trống &nbsp;&nbsp;&nbsp; 🔴 Đang sử dụng")

# ---------- Sidebar ----------
with st.sidebar:
    st.header("⚙️ Hệ thống")
    st.text_input("Tên bãi đỗ", "Smart Parking")
    st.selectbox("Camera", ["Camera 01", "Camera 02"])
    st.selectbox("Chế độ", ["Demo", "AI Detection"])
    st.button("🔄 Làm mới dữ liệu", use_container_width=True)

    st.divider()
    st.caption("AI modules")
    st.write("🚗 Vehicle Detection: YOLO")
    st.write("🔎 License Plate: YOLO")
    st.write("🔤 OCR: PaddleOCR")
    st.write("📹 Video: OpenCV")

