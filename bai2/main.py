from disk_manager import calculate_disk_blocks
from io_helper import safe_create_dir
from time_validator import parse_and_inspect_date

raw_files = [
    {
        "filename": "pod_ep1.mp3",
        "size_bytes": 4500,
        "duration_sec": 180,
        "upload_at": "2026-06-10"
    },

    {
        "filename": "movie_trailer.mp4",
        "size_bytes": 105000,
        "duration_sec": 145,
        "upload_at": "2026-06-31"
    },

    {
        "filename": "clip_short.mp4",
        "size_bytes": 8200,
        "duration_sec": 15,
        "upload_at": "2026-05-15"
    }
]

success = 0
print("====== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA =====")
safe_create_dir("media_vault")
print("[SYSTEM] Kiểm tra hạ tầng lưu trữ......Hoàn tất.")
print("---------------------------------------------------")

for file in raw_files:
    print()
    print("[TỆP TIN:", file["filename"] + "]")
    date = parse_and_inspect_date(
        file["upload_at"]
    )

    if date == False:
        print(" + Trạng thái phân loại: 🔴 THẤT BẠI")
        print(" + Lỗi: Định dạng ngày upload", file["upload_at"],"không tồn tại")
    else:
        blocks = calculate_disk_blocks(
            file["size_bytes"]
        )

        print(" + Dung lượng thực tế:",file["size_bytes"],"Bytes")

        print(" + Số khối phân vùng:",blocks,"Blocks")

        if file["filename"].endswith(".mp3"):
            print(" + Trạng thái phân loại: 🟢 HỢP LỆ (Lưu trữ vào thư mục 'audio')")
        else:
            print(" + Trạng thái phân loại: 🟢 HỢP LỆ (Lưu trữ vào thư mục 'video')")

        success = success + 1

print("=============================================================")
print(
    "TIẾN ĐỘ QUÉT: success /3 tệp tin thành công."
)
