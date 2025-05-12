import streamlit as st

st.set_page_config(page_title="Sistem Pendukung Keputusan Stok Makanan di Kapal")

st.title("🛳️ Sistem Pendukung Keputusan")
st.subheader("Efisiensi Manajemen Stok Makanan di Kapal")

st.markdown("Masukkan kondisi stok makanan berdasarkan kategori di bawah ini:")

# Input untuk stok 3 bulan
st.markdown("### 🔹 Data Bahan Makanan Stok 3 Bulan")
beras = st.selectbox("Jumlah Beras", ["kurang", "cukup", "berlebih"])
daging = st.selectbox("Jumlah Daging", ["kurang", "cukup", "berlebih"])
ikan = st.selectbox("Jumlah Ikan", ["kurang", "cukup", "berlebih"])

# Input untuk stok 1 bulan
st.markdown("### 🔹 Data Bahan Makanan Stok 1 Bulan")
sayur = st.selectbox("Jumlah Sayur", ["kurang", "cukup", "berlebih"])
buah = st.selectbox("Jumlah Buah", ["kurang", "cukup", "berlebih"])

# Input makanan cadangan
st.markdown("### 🔹 Makanan Cadangan")
cadangan = st.radio("Apakah ada makanan cadangan?", ["ada", "tidak"])

# Fungsi untuk menentukan status stok 3 bulan
def status_stok_3b(beras, daging, ikan):
    if beras == daging == ikan == "cukup":
        return "Cukup"
    elif beras == daging == ikan == "berlebih":
        return "Berlebih"
    elif beras == daging == ikan == "kurang":
        return "Kurang"
    elif "kurang" in [beras, daging, ikan]:
        return "Ada yang kurang"
    elif "berlebih" in [beras, daging, ikan]:
        return "Ada yang berlebih"
    return "Cukup"

# Fungsi untuk status stok 1 bulan
def status_stok_1b(sayur, buah):
    if sayur == buah == "cukup":
        return "Cukup"
    elif sayur == buah == "kurang":
        return "Kurang"
    elif sayur == buah == "berlebih":
        return "Berlebih"
    elif "kurang" in [sayur, buah]:
        return "Ada yang kurang"
    elif "berlebih" in [sayur, buah]:
        return "Ada yang berlebih"
    return "Cukup"

# Penentuan status masing-masing
stok_3b = status_stok_3b(beras, daging, ikan)
stok_1b = status_stok_1b(sayur, buah)

# Fungsi inferensi akhir
def keputusan(stok_3b, stok_1b, cadangan):
    if stok_3b == "Cukup" and stok_1b == "Cukup":
        return "Seluruh Stok Cukup"
    elif stok_3b == "Kurang" and stok_1b == "Kurang":
        return "Seluruh Stok Kurang"
    elif stok_3b == "Berlebih" and stok_1b == "Berlebih":
        return "Seluruh Stok Berlebih"
    elif "kurang" in stok_3b.lower() or "kurang" in stok_1b.lower():
        return "Terdapat Stok yang Kurang"
    elif "berlebih" in stok_3b.lower() or "berlebih" in stok_1b.lower():
        return "Terdapat Stok yang Berlebih"
    else:
        return "Tidak Diketahui"

# Tombol untuk prediksi
if st.button("🔍 Lihat Keputusan"):
    hasil = keputusan(stok_3b, stok_1b, cadangan)
    st.success(f"**Keputusan Sistem:** {hasil}")
    st.markdown(f"- Status Stok 3 Bulan: **{stok_3b}**")
    st.markdown(f"- Status Stok 1 Bulan: **{stok_1b}**")
    st.markdown(f"- Makanan Cadangan: **{cadangan}**")

