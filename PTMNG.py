import os
def get_next_id(file_path="file.txt"):
    max_id, cnt_photo = 0, 0
    with open(file_path, "rb") as f:
        while True:
            header = f.readline()
            if not header:
                break
            if header.startswith(b"photo "):
                parts = header.decode(errors="ignore").split()
                if len(parts) < 3:
                    continue
                try:
                    photo_id = int(parts[1])
                    cnt_photo += 1
                    max_id = max(max_id, photo_id)
                except:
                    continue
                size = int(parts[2])
                f.read(size)
    return max_id + 1, cnt_photo

def add_photo(url: str):
    photo_id, cnt_photo = get_next_id()
    if int(cnt_photo) >= 10:
        print("file is full!!!")
        return
    with open(url, "rb") as p:
        binary_data = p.read()
    with open("file.txt", "ab") as f:
        header = f"photo {photo_id} {len(binary_data)}\n".encode()
        f.write(header)
        f.write(binary_data)
    print(f"Saved as photo {photo_id}") 

def search_photo(photo_id,file_path="file.txt"):
    with open(file_path, "rb") as f:
        while True:
            header = f.readline()
            if not header:
                break
            if header.startswith(b"photo "):
                parts = header.decode().strip().split()
                if len(parts) < 3:
                    continue
                current_id = int(parts[1])
                size = int(parts[2])
                binary_data = f.read(size)
                if current_id == photo_id:
                    filename = f"restored_{photo_id}.jpg"
                    with open(filename, "wb") as img:
                        img.write(binary_data)
                    print(f"✅ Photo {photo_id} saved as {filename}")
                    return
        print("❌ Photo not found")

def delete_photo(photo_id, file_path="file.txt"):
    temp_file = "temp.txt"
    found = False
    with open(file_path, "rb") as f, open(temp_file, "wb") as out:
        while True:
            header = f.readline()
            if not header:
                break
            if header.startswith(b"photo "):
                parts = header.decode(errors="ignore").strip().split()
                if len(parts) < 3:
                    continue
                try:
                    current_id = int(parts[1])
                    size = int(parts[2])
                except:
                    continue
                binary_data = f.read(size)
                if current_id == photo_id:
                    found = True
                    continue
                out.write(header)
                out.write(binary_data)
    os.replace(temp_file, file_path)
    if found:
        print(f"✅ Photo {photo_id} deleted")
    else:
        print("❌ Photo not found")

while True:
    
    op = input("Enter operation 1 add photo 2 search photo 3 remove photo 4 exit : ")

    if op == '1':
        url = input("Enter Photos Path : ")
        add_photo(url)
    elif op == '2':
        photo_id = int(input("enter photo id : "))
        search_photo(photo_id)
    elif op == '3':
        photo_id = int(input("enter photo id : "))
        delete_photo(photo_id)
    else:
        exit()