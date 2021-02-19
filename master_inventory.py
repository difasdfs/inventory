# BLOCK
cabang = input('Nama File : ')

# file = open('daftar_barang.csv')
sales = open(cabang + '.csv')

# CABANG
# cabang = ['metro','antapani','cisitu','jatinangor','sukabirus','sukajadi','sukapura','unjani']

# BLOCK
# variabel product assembly
ayam_crispy = 0
paper_cost_takeaway_l = 0
paper_cost_takeaway_m = 0
paper_cost_takeaway_paper_bag = 0
packaging_frozen = 0
paper_cost_dine_in = 0
ayam_geprek_crispy = 0
upsize_double_chiken_online = 0
upsize_double_chiken_dine_in = 0
topping_bbq_cheese = 0
topping_bbq_gravy = 0
topping_crisbar = 0
topping_matah = 0
topping_mamah = 0
topping_tomat = 0
topping_manis = 0
topping_goang = 0
topping_keju = 0
topping_crisbar_madu = 0
topping_crisbar_frozen = 0
topping_mamah_frozen = 0
kuah_tongseng = 0
nasi_dine_in = 0
es_teh_dine_in = 0
lemon_tea_dine_in = 0
lemonade_dine_in = 0
milo_dine_in = 0
orange_dine_in = 0
tahu_crispy = 0
tempe_crispy = 0
terong_crispy = 0
telur_sayur = 0
dua_chicken_skin_crispy = 0
nugget = 0
kerupuk = 0
kurma = 0
puding_milo_dino = 0
lalab = 0
nasi_takeaway = 0
es_teh_takeaway = 0
lemon_tea_takeaway = 0
lemonade_takeaway = 0
milo_takeaway = 0
minum = 0
orange_takeaway = 0
sjora_mango_peach = 0
kol_crispy = 0

# BLOCK
# sku_nama = {}

# for isi in file.readlines():
#     isi = isi.split(',')
#     sku = isi[1]
#     nama_item = isi[2]
    
#     if sku == 'SKU':
#         continue
    
#     sku_nama[sku] = nama_item

# BLOCK
for penjualan in sales.readlines():
    penjualan = penjualan.split(',')
    
    if penjualan[1] == 'SKU':
        continue
        
    nama_item = penjualan[0]
    sku = penjualan[1]
    barang_terjual = int(penjualan[3].split('.')[0])
    
    # (Makan Driver) Paket Ayam Crispy + Nasi + Es Teh Manis (DINE IN)
    if sku == '10711090':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        
    # 3 Ayam Crisbar + 3 Nasi + 3 Es Teh (DINE IN)
    elif sku == '10311190':
        paper_cost_dine_in += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        topping_crisbar += 3*barang_terjual
        nasi_dine_in += 3*barang_terjual
        es_teh_dine_in += 3*barang_terjual

    # 3 Ayam Crispy+ 3 Nasi + 3 Es Teh (DINE IN)
    elif sku == '10311090':
        ayam_geprek_crispy += 3*barang_terjual
        nasi_dine_in += 3*barang_terjual
        es_teh_dine_in += 3*barang_terjual
        
    # 3 Kol Crispy (DINE IN)
    elif sku == '70000100':
        kol_crispy += 3*barang_terjual
        
    # Ayam Crisbar (DINE IN)
    elif sku == '10011100':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        
    # Ayam Crispy (DINE IN)
    elif sku == '10010000':
        ayam_crispy += barang_terjual
        paper_cost_dine_in += barang_terjual
        
    # Ayam Crispy Geprek (DINE IN)
    elif sku == '10011000':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        
    # Ayam Goang (DINE IN)
    elif sku == '10011700':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        
    # Ayam Keju (DINE IN)
    elif sku == '10011500':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        
    # Ayam Mamah (DINE IN)
    elif sku == '10011300':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        
    # Ayam Manis (DINE IN)
    elif sku == '10011600':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        
    # Ayam Matah (DINE IN)
    elif sku == '10011200':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        
    # Ayam Tomat (DINE IN)
    elif sku == '10011400':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        
    # Chiken Skin (DINE IN)
    elif sku == '70000050':
        dua_chicken_skin_crispy += barang_terjual
        
    # Crisbar + Es Teh + 1 Porsi Kol Crispy (DINE IN)
    elif sku == '10611490':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        kol_crispy += barang_terjual
        
    # Crisbar + Es Teh + Gratis 2 Kulit (DINE IN)
    elif sku == '10611190':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Crisbar + Es Teh + Gratis Tahu dan Tempe (DINE IN)
    elif sku == '10611290':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        
    # Crisbar + Lemontea/Lemonade + Gratis Tahu dan Tempe (DINE IN)
    elif sku == '10611260':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        lemon_tea_dine_in += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        
    # Crisbar + LemoTea/Lemonade + 1 Porsi Kol Crispy (DINE IN)
    elif sku == '10611460':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        lemon_tea_dine_in += barang_terjual
        kol_crispy += barang_terjual
        
    # Crisbar + LemoTea/Lemonade + Gratis 2 Kulit (DINE IN)
    elif sku == '10611160':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        lemon_tea_dine_in += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Crisbar + Milo + 1 Porsi Kol Crispy (DINE IN)
    elif sku == '10611470':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        kol_crispy += barang_terjual
        
    # Crisbar + Milo + Gratis 2 Kulit (DINE IN)
    elif sku == '10611170':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Crisbar + Milo + Gratis Tahu dan Tempe (DINE IN)
    elif sku == '10611270':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        
    # Crisbar + Orange + 1 Porsi Kol Crispy (DINE IN)
    elif sku == '10611480':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        kol_crispy += barang_terjual
        
    # Crisbar + Orange + Gratis 2 Kulit (DINE IN)
    elif sku == '10611180':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Crisbar + Orange + Gratis Tahu dan Tempe (DINE IN)
    elif sku == '10611280':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        
    # Crispy + Es Teh + Gratis 2 Kulit (DINE IN)
    elif sku == '10611090':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Crispy + LemonTea/Lemonade + Gratis 2 Kulit (DINE IN)
    elif sku == '10611060':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_dine_in += barang_terjual
        lemon_tea_dine_in += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Crispy + Milo + Gratis 2 Kulit (DINE IN)
    elif sku == '10611070':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Crispy + Orange + Gratis 2 Kulit (DINE IN)
    elif sku == '10611080':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Es Teh Manis (DINE IN)
    elif sku == '80000090':
        es_teh_dine_in += barang_terjual
        
    # Frozen Crisbar (DINE IN)
    elif sku == '1031110':
        packaging_frozen += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        
    # Frozen Sambal Mamah (DINE IN)
    elif sku == '1031130':
        packaging_frozen += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        
    # Kerupuk (DINE IN)
    elif sku == '70000080':
        kerupuk += barang_terjual
        
    # Kuah Tongseng (DINE IN)
    elif sku == '70000060':
        kuah_tongseng += barang_terjual
        
    # Lemon Tea (DINE IN)
    elif sku == '80000060':
        lemon_tea_dine_in += barang_terjual
        
    # Lemonade (DINE IN)
    elif sku == '80000050':
        lemonade_dine_in += barang_terjual
        
    # Milo (DINE IN)
    elif sku == '80000070':
        milo_dine_in += barang_terjual
        
    # Nasi (DINE IN)
    elif sku == '70000000':
        nasi_dine_in += barang_terjual
        
    # Nugget (DINE IN)
    elif sku == '70000070':
        nugget += barang_terjual
        
    # Orange (DINE IN)
    elif sku == '80000080':
        orange_dine_in += barang_terjual
        
    # Paket 4 Chiken Skin + Es Teh (DINE IN)
    elif sku == '10200190':
        paper_cost_dine_in += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        
    # Paket 4 Chiken Skin + Lemon (DINE IN)
    elif sku == '10200160':
        paper_cost_dine_in += barang_terjual
        nasi_dine_in += barang_terjual
        lemon_tea_dine_in += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        
    # Paket 4 Chiken Skin + Milo (DINE IN)
    elif sku == '10200170':
        paper_cost_dine_in += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        
    # Paket 4 Chiken Skin + Orange (DINE IN)
    elif sku == '10200180':
        paper_cost_dine_in += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        
    # Paket Ayam Crisbar Es Teh (DINE IN)
    elif sku == '10111190':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        
    # Paket Ayam Crisbar Lemontea/Lemonade (DINE IN)
    elif sku == '10111160':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        lemonade_dine_in += barang_terjual
        
    # Paket Ayam Crisbar Milo (DINE IN)
    elif sku == '10111170':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        
    # Paket Ayam Crisbar Orange (DINE IN)
    elif sku == '10111180':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        
    # Paket Ayam Geprek Crispy Es Teh (DINE IN)
    elif sku == '10111090':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        
    # Paket Ayam Geprek Crispy Lemontea/Lemonade (DINE IN)
    elif sku == '10111060':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_dine_in += barang_terjual
        lemonade_dine_in += barang_terjual
        
    # Paket Ayam Geprek Crispy Milo (DINE IN)
    elif sku == '10111070':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        
    # Paket Ayam Geprek Crispy Orange (DINE IN)
    elif sku == '10111080':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        
    # Paket Ayam Goang Es Teh (DINE IN)
    elif sku == '10111790':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual

    # Paket Ayam Goang Lemontea/Lemonade (DINE IN)
    elif sku == '10111760':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_dine_in += barang_terjual
        lemonade_dine_in += barang_terjual
        
    # Paket Ayam Goang Milo (DINE IN)
    elif sku == '10111770':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        
    # Paket Ayam Goang Orange (DINE IN)
    elif sku == '10111780':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        
    # Paket Ayam Keju Es Teh (DINE IN)
    elif sku == '10111590':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        
    # Paket Ayam Keju Lemontea/Lemonade (DINE IN)
    elif sku == '10111560':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_dine_in += barang_terjual
        lemonade_dine_in += barang_terjual
        
    # Paket Ayam Keju Milo (DINE IN)
    elif sku == '10111570':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        
    # Paket Ayam Keju Orange (DINE IN)
    elif sku == '10111580':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        
    # Paket Ayam Mamah Es Teh (DINE IN)
    elif sku == '10111390':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        
    # Paket Ayam Mamah Lemontea/Lemonade (DINE IN)
    elif sku == '10111360':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_dine_in += barang_terjual
        lemonade_dine_in += barang_terjual
        
    # Paket Ayam Mamah Milo (DINE IN)
    elif sku == '10111370':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        
    # Paket Ayam Mamah Orange (DINE IN)
    elif sku == '10111380':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        
    # Paket Ayam Manis Es Teh (DINE IN)
    elif sku == '10111690':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        
    # Paket Ayam Manis Lemontea/Lemonade (DINE IN)
    elif sku == '10111660':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_dine_in += barang_terjual
        lemonade_dine_in += barang_terjual
        
    # Paket Ayam Manis Milo (DINE IN)
    elif sku == '10111670':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        
    # Paket Ayam Manis Orange (DINE IN)
    elif sku == '10111680':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        
    # Paket Ayam Matah Es Teh (DINE IN)
    elif sku == '10111290':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        
    # Paket Ayam Matah Lemontea/Lemonade (DINE IN)
    elif sku == '10111260':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_dine_in += barang_terjual
        lemonade_dine_in += barang_terjual
        
    # Paket Ayam Matah Milo (DINE IN)
    elif sku == '10111270':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        
    # Paket Ayam Matah Orange (DINE IN)
    elif sku == '10111280':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        
    # Paket Ayam Saos BBQ Cheese Es Teh (DINE IN)
    elif sku == '10112190':
        ayam_crispy += barang_terjual
        paper_cost_dine_in += barang_terjual
        topping_bbq_cheese += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        
    # Paket Ayam Saos BBQ Cheese Milo (DINE IN)
    elif sku == '10112170':
        ayam_crispy += barang_terjual
        paper_cost_dine_in += barang_terjual
        topping_bbq_cheese += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        
    # Paket Ayam Saos BBQ Cheese Orange (DINE IN)
    elif sku == '10112180':
        ayam_crispy += barang_terjual
        paper_cost_dine_in += barang_terjual
        topping_bbq_cheese += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        
    # Paket Ayam Saos Gravy Es Teh (DINE IN)
    elif sku == '10112290':
        ayam_crispy += barang_terjual
        paper_cost_dine_in += barang_terjual
        topping_bbq_gravy += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        
    # Paket Ayam Saos Gravy Milo (DINE IN)
    elif sku == '10112270':
        ayam_crispy += barang_terjual
        paper_cost_dine_in += barang_terjual
        topping_bbq_gravy += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        
    # Paket Ayam Saos Gravy Orange (DINE IN)
    elif sku == '10112280':
        ayam_crispy += barang_terjual
        paper_cost_dine_in += barang_terjual
        topping_bbq_gravy += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        
    # Paket Ayam Tomat Es Teh (DINE IN)
    elif sku == '10111490':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        
    # Paket Ayam Tomat Lemontea/Lemonade (DINE IN)
    elif sku == '10111460':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_dine_in += barang_terjual
        lemonade_dine_in += barang_terjual
        
    # Paket Ayam Tomat Milo (DINE IN)
    elif sku == '10111470':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        
    # Paket Ayam Tomat Orange (DINE IN)
    elif sku == '10111480':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        
    # Paket Side Dish Es Teh (DINE IN)
    elif sku == '10200290':
        paper_cost_dine_in += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        
    # Paket Side Dish Lemon (DINE IN)
    elif sku == '10200260':
        paper_cost_dine_in += barang_terjual
        nasi_dine_in += barang_terjual
        lemonade_dine_in += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        
    # Paket Side Dish Milo (DINE IN)
    elif sku == '10200270':
        paper_cost_dine_in += barang_terjual
        nasi_dine_in += barang_terjual
        milo_dine_in += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        
    # Paket Side Dish Orange (DINE IN)
    elif sku == '10200280':
        paper_cost_dine_in += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        
    # Pudding Milo Dino (DINE IN)
    elif sku == '50000020':
        puding_milo_dino += barang_terjual
        
    # Raksasa Crisbar + Tahu + Tempe + Terong+ Telur + Kulit+ Es Teh (DINE IN)
    elif sku == '10211090':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Raksasa Crispy + Tahu + Tempe + Terong+ Telur + Kulit+ Es Teh (DINE IN)
    elif sku == '10211190':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Tahu Crispy (DINE IN)
    elif sku == '70000020':
        tahu_crispy += barang_terjual
        
    # Telur Sayur (DINE IN)
    elif sku == '70000040':
        telur_sayur += barang_terjual
        
    # Tempe Crispy (DINE IN)
    elif sku == '70000010':
        tempe_crispy += barang_terjual
        
    # Terong Crispy (DINE IN)
    elif sku == '70000030':
        terong_crispy += barang_terjual
        
    # Topping BBQ Cheese (DINE IN)
    elif sku == '9000210':
        topping_bbq_cheese += barang_terjual
        
    # Topping BBQ Gravy (DINE IN)
    elif sku == '9000220':
        topping_bbq_gravy += barang_terjual
        
    # Topping Crisbar (DINE IN)
    elif sku == '90000100':
        topping_crisbar += barang_terjual
        
    # Topping Keju (DINE IN)
    elif sku == '90000500':
        topping_keju += barang_terjual
        
    # Topping Mamah (DINE IN)
    elif sku == '90000300':
        topping_mamah += barang_terjual
        
    # Topping Manis (DINE IN)
    elif sku == '90000600':
        topping_manis += barang_terjual
        
    # Topping Matah (DINE IN)
    elif sku == '90000200':
        topping_matah += barang_terjual
        
    # Topping Tomat (DINE IN)
    elif sku == '90000400':
        topping_tomat += barang_terjual
        
    # 2 Ayam Crisbar + 3 Ayam Sambal Mix (GO FOOD)
    # ini sambelnya ga bisa ditrack
    elif sku == '10310203':
        ayam_crispy += 5*barang_terjual
        paper_cost_takeaway_m += 5*barang_terjual
        topping_crisbar += 2*barang_terjual
        topping_matah += barang_terjual
        topping_mamah += barang_terjual
        topping_tomat += barang_terjual
        
    # (Driver)Paket Ayam Crispy + Lalab + Es Teh Online (GO FOOD)
    elif sku == '10711093':
        ayam_crispy += barang_terjual
        paper_cost_takeaway_l += barang_terjual
        lalab += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # 3 Ayam Crisbar + 3 Nasi + 3 Es Teh (GO FOOD)
    elif sku == '10311193':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        topping_crisbar += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        es_teh_takeaway += 3*barang_terjual
        
    # 3 Ayam Crisbar + 3 Nasi + 3 LemonTea/Lemonade (GO FOOD)
    elif sku == '10311163':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        topping_crisbar += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        lemon_tea_takeaway += 3*barang_terjual
        
    # 3 Ayam Crisbar + 3 Nasi + 3 Milo (GO FOOD)
    elif sku == '10311173':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        topping_crisbar += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        milo_takeaway += 3*barang_terjual
        
    # 3 Ayam Crisbar + 3 Nasi + 3 Orange (GO FOOD)
    elif sku == '10311183':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        topping_crisbar += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        orange_takeaway += 3*barang_terjual
        
    # 3 Ayam Crispy + 3 Nasi + 3 Es Teh (GO FOOD)
    elif sku == '10311093':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        es_teh_takeaway += 3*barang_terjual
        
    # 3 Ayam Crispy + 3 Nasi + 3 LemonTea/Lemonade (GO FOOD)
    elif sku == '10311063':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        es_teh_dine_in += 3*barang_terjual
        lemon_tea_takeaway += 3*barang_terjual
        
    # 3 Ayam Crispy + 3 Nasi + 3 Milo (GO FOOD)
    elif sku == '10311073':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        es_teh_dine_in += 3*barang_terjual
        milo_takeaway += 3*barang_terjual
        
    # 3 Ayam Crispy + 3 Nasi + 3 Orange (GO FOOD)
    elif sku == '10311083':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        es_teh_dine_in += 3*barang_terjual
        orange_takeaway += 3*barang_terjual
        
    # 3 Kol Crispy Online (GO FOOD)
    elif sku == '70000103':
        kol_crispy += 3*barang_terjual
        
    # 4 Ayam Crisbar Original/Geprek Ala Carte (GO FOOD)
    elif sku == '10310103':
        paper_cost_takeaway_m += 4*barang_terjual
        ayam_geprek_crispy += 4*barang_terjual
        topping_crisbar += 4*topping_crisbar
        
    # 4 Ayam Crispy Original/Geprek Ala Carte (GO FOOD)
    elif sku == '10310003':
        paper_cost_takeaway_m += 4*barang_terjual
        ayam_geprek_crispy += 4*barang_terjual
        
    # Ayam Crispy Geprek Online (GO FOOD)
    elif sku == '10011003':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        
    # Ayam Goang Online (GO FOOD)
    elif sku == '10011703':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        
    # Ayam Keju Online (GO FOOD)
    elif sku == '10011503':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        
    # Ayam Mamah Online (GO FOOD)
    elif sku == '10011303':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        
    # Ayam Manis Online (GO FOOD)
    elif sku == '10011603':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        
    # Ayam Matah Online (GO FOOD)
    elif sku == 'Ayam Matah Online':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        
    # Ayam Tomat Online (GO FOOD)
    elif sku == '10011403':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        
    # Chiken Skin Crispy Online (GO FOOD)
    elif sku == '70000053':
        dua_chicken_skin_crispy += barang_terjual
        
    # Crisbar + Es Teh + 1 Porsi Kol Crispy (GO FOOD)
    elif sku == '10611493':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        kol_crispy += barang_terjual
        
    # Crisbar + Es Teh + Gratis 2 Kulit (GO FOOD)
    elif sku == '10611193':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Crisbar + Es Teh + Gratis Tahu Tempe (GO FOOD)
    elif sku == '10611293':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Crisbar + Lemontea/Lemonade + Gratis Tahu dan Tempe (GO FOOD)
    elif sku == '10611263':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Crisbar + LemoTea/Lemonade + 1 Porsi Kol Crispy (GO FOOD)
    elif sku == '10611463':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        kol_crispy += barang_terjual
        
    # Crisbar + LemoTea/Lemonade + Gratis 2 Kulit (GO FOOD)
    elif sku == '10611163':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Crisbar + Milo + 1 Porsi Kol Crispy (GO FOOD)
    elif sku == '10611473':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        kol_crispy += barang_terjual
        
    # Crisbar + Milo + Gratis 2 Kulit (GO FOOD)
    elif sku == '10611173':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Crisbar + Milo + Gratis Tahu Tempe (GO FOOD)
    elif sku == '10611273':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        
    # Crisbar + Orange + 1 Porsi Kol Crispy (GO FOOD)
    elif sku == '10611483':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        kol_crispy += barang_terjual
        
    # Crisbar + Orange + Gratis 2 Kulit (GO FOOD)
    elif sku == '10611183':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Crisbar + Orange + Gratis Tahu dan Tempe (GO FOOD)
    elif sku == '10611283':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        
    # Crispy + Es Teh + Gratis 2 Kulit (GO FOOD)
    elif sku == '10611093':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Crispy + LemonTea/Lemonade + Gratis 2 Kulit (GO FOOD)
    elif sku == '10611063':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Crispy + Milo + Gratis 2 Kulit (GO FOOD)
    elif sku == '10611073':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Crispy + Orange + Gratis 2 Kulit (GO FOOD)
    elif sku == '10611083':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Es Teh Manis Online (GO FOOD)
    elif sku == '80000093':
        es_teh_takeaway += barang_terjual
        
    # Frozen Ayam Geprek Crisbar (GO FOOD) 
    elif sku == '1031113':
        packaging_frozen += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        
    # Frozen Ayam Sambal Mamah (GO FOOD)
    elif sku == '1031133':
        packaging_frozen += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        
    # Kerupuk Online (GO FOOD)
    elif sku == '70000083':
        kerupuk += barang_terjual
        
    # Lemon Tea Online (GO FOOD)
    elif sku == '80000063':
        lemon_tea_takeaway += barang_terjual
        
    # Lemonade Online (GO FOOD)
    elif sku == '80000053':
        lemonade_takeaway += barang_terjual
        
    # Milo Online (GO FOOD)
    elif sku == '80000073':
        milo_takeaway += barang_terjual
        
    # Nasi Ayam Crisbar (GO FOOD)
    elif sku == '10111103':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Crispy (GO FOOD)
    elif sku == '10111003':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Goang (GO FOOD)
    elif sku == '10111703':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Keju (GO FOOD)
    elif sku == '10111503':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Mamah (GO FOOD)
    elif sku == '10111303':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Manis (GO FOOD)
    elif sku == '10111603':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Matah (GO FOOD)
    elif sku == '10111203':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Tomat (GO FOOD)
    elif sku == '10111403':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Online (GO FOOD)
    elif sku == '70000003':
        nasi_takeaway += barang_terjual
        
    # Orange Online (GO FOOD)
    elif sku == '80000083':
        orange_takeaway += barang_terjual
        
    # P.Crisbar+P.Keju+2 Es Teh+Gratis 2 Tempe 4 Kulit Chiken Skin (GO FOOD)
    elif sku == '10611393':
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += barang_terjual
        topping_keju += barang_terjual
        tempe_crispy += 2*barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        nasi_takeaway += 2*barang_terjual
        es_teh_takeaway += 2*barang_terjual
        
    # P.Crisbar+P.Keju+2 LemonTea/Lemonade+Gratis 2 Tempe 4 Kulit (GO FOOD)
    elif sku == '10611363':
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += barang_terjual
        topping_keju += barang_terjual
        tempe_crispy += 2*barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        nasi_takeaway += 2*barang_terjual
        lemon_tea_takeaway += 2*barang_terjual
        
    # P.Crisbar+P.Keju+2 Milo+Gratis 2 Tempe 4 Chiken Skin (GO FOOD)
    elif sku == '10611373':
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += barang_terjual
        topping_keju += barang_terjual
        tempe_crispy += 2*barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        nasi_takeaway += 2*barang_terjual
        milo_takeaway += 2*barang_terjual
        
    # P.Crisbar+P.Keju+2 Orange+Gratis 2 Tempe 4 Kulit (GO FOOD)
    elif sku == '10611383':
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += barang_terjual
        topping_keju += barang_terjual
        tempe_crispy += 2*barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        nasi_takeaway += 2*barang_terjual
        orange_takeaway += 2*barang_terjual
        
    # Paket 4 Chiken Skin + Es Teh Online (GO FOOD)
    elif sku == '10200193':
        paper_cost_takeaway_l += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Paket 4 Chiken Skin + Lemon Online (GO FOOD)
    elif sku == '10200163':
        paper_cost_takeaway_l += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Paket 4 Chiken Skin + Milo Online (GO FOOD)
    elif sku == '10200173':
        paper_cost_takeaway_l += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Paket 4 Chiken Skin + Orange Online (GO FOOD)
    elif sku == '10200183':
        paper_cost_takeaway_l += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Paket Ayam Crisbar Es Teh Online (GO FOOD)
    elif sku == '10111193':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Paket Ayam Crisbar Lemon Tea/Lemonade Online (GO FOOD)
    elif sku == '10111163':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Paket Ayam Crisbar Milo Online (GO FOOD)
    elif sku == '10111173':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Paket Ayam Crisbar Orange Online (GO FOOD)
    elif sku == '10111183':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Paket Ayam Geprek Crispy Es Teh Online (GO FOOD)
    elif sku == '10111093':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Paket Ayam Geprek Crispy Lemon Tea/Lemonade Online (GO FOOD)
    elif sku == '10111063':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Paket Ayam Geprek Crispy Milo Online (GO FOOD)
    elif sku == '10111073':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Paket Ayam Geprek Crispy Orange Online (GO FOOD)
    elif sku == '10111083':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Paket Ayam Goang Es Teh Online (GO FOOD)
    elif sku == '10111793':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Paket Ayam Goang Lemon Tea/Lemonade (GO FOOD)
    elif sku == '10111763':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Paket Ayam Goang Milo Online (GO FOOD)
    elif sku == '10111773':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Paket Ayam Goang Orange Online (GO FOOD)
    elif sku == '10111783':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Paket Ayam Keju Es Teh online (GO FOOD)
    elif sku == '10111593':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Paket Ayam Keju Lemon Tea/Lemonade Online (GO FOOD)
    elif sku == '10111563':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Paket Ayam Keju Milo Online (GO FOOD)
    elif sku == '10111573':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Paket Ayam Keju Orange Online (GO FOOD)
    elif sku == '10111583':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Paket Ayam Mamah Es Teh Online (GO FOOD)
    elif sku == '10111393':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Paket Ayam Mamah Lemon Tea/Lemonade Online (GO FOOD)
    elif sku == '10111363':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Paket Ayam Mamah Milo Online (GO FOOD)
    elif sku == '10111373':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Paket Ayam Mamah Orange Online (GO FOOD)
    elif sku == '10111383':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Paket Ayam Manis Es Teh Online (GO FOOD)
    elif sku == '10111693':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Paket Ayam Manis Lemon Tea/Lemonade Online (GO FOOD)
    elif sku == '10111663':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Paket Ayam Manis Milo Online (GO FOOD)
    elif sku == '10111673':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Paket Ayam Manis Orange Online (GO FOOD)
    elif sku == '10111683':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Paket Ayam Matah Es Teh Online (GO FOOD)
    elif sku == '10111293':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Paket Ayam Matah Lemon Tea/Lemonade Online (GO FOOD)
    elif sku == '10111263':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Paket Ayam Matah Milo Online (GO FOOD)
    elif sku == '10111273':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Paket Ayam Matah Orange Online (GO FOOD)
    elif sku == '10111283':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Paket Ayam Tomat Es Teh Online (GO FOOD)
    elif sku == '10111493':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Paket Ayam Tomat Lemon Tea/Lemonade Online (GO FOOD)
    elif sku == '10111463':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Paket Ayam Tomat Milo Online (GO FOOD)
    elif sku == '10111473':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Paket Ayam Tomat Orange Online (GO FOOD)
    elif sku == '10111483':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Paket Side Dish Es Teh Online (GO FOOD)
    elif sku == '10200293':
        paper_cost_takeaway_l += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Paket Side Dish Lemon Online (GO FOOD)
    elif sku == '10200263':
        paper_cost_takeaway_l += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Paket Side Dish Milo Online (GO FOOD)
    elif sku == '10200273':
        paper_cost_takeaway_l += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Paket Side Dish Orange Online (GO FOOD)
    elif sku == '10200283':
        paper_cost_takeaway_l += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Pudding Milo Dino Online (GO FOOD)
    elif sku == '50000023':
        puding_milo_dino += barang_terjual
        
    # Raksasa Crisbar + Tahu + Tempe + Terong + Telur + Kulit + Es Teh (GO FOOD)
    elif sku == '10211093':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Raksasa Crisbar + Tahu + Tempe + Terong + Telur + Kulit + Milo (GO FOOD)
    elif sku == '10211073':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Raksasa Crisbar + Tahu + Tempe + Terong+ Telur + Kulit+ Lemon (GO FOOD)
    elif sku == '10211063':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemonade_takeaway += barang_terjual
        
    # Raksasa Crisbar + Tahu + Tempe + Terong+ Telur + Kulit+ Orange (GO FOOD)
    elif sku == '10211083':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Raksasa Crispy + Tahu + Tempe + Terong + Telur + Kulit + Es Teh (GO FOOD)
    elif sku == '10211193':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Raksasa Crispy + Tahu + Tempe + Terong + Telur + Kulit + Milo (GO FOOD)
    elif sku == '10211173':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
    
    # Raksasa Crispy + Tahu + Tempe + Terong + Telur + Kulit + Orange (GO FOOD)
    elif sku == '10211183':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Raksasa Crispy + Tahu + Tempe + Terong+ Telur + Kulit+ Lemon (GO FOOD)
    elif sku == '10211163':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemonade_takeaway += barang_terjual
        
    # Raksasa Keju + Tahu + Tempe + Terong + Telur + Kulit + Es Teh (GO FOOD)
    elif sku == '10211393':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Raksasa Keju + Tahu + Tempe + Terong + Telur + Kulit + Milo (GO FOOD)
    elif sku == '10211373':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Raksasa Keju + Tahu + Tempe + Terong + Telur + Kulit + Orange (GO FOOD)
    elif sku == '10211383':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Raksasa Keju + Tahu + Tempe + Terong+ Telur + Kulit+ Lemon (GO FOOD)
    elif sku == '10211363':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Raksasa Manis + Tahu + Tempe + Terong + Telur + Kulit + Es Teh (GO FOOD)
    elif sku == '10211293':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # Raksasa Manis + Tahu + Tempe + Terong + Telur + Kulit+ Lemon (GO FOOD)
    elif sku == '10211263':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        
    # Raksasa Manis + Tahu + Tempe + Terong+ Telur + Kulit+ Milo (GO FOOD)
    elif sku == '10211273':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        
    # Raksasa Manis + Tahu + Tempe + Terong+ Telur + Kulit+ Orange (GO FOOD)
    elif sku == '10211283':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        
    # Tahu Crispy Online (GO FOOD)
    elif sku == '70000023':
        tahu_crispy += barang_terjual
        
    # Telur Sayur Online (GO FOOD)
    elif sku == '70000043':
        telur_sayur += barang_terjual
        
    # Tempe Crispy Online (GO FOOD)
    elif sku == '70000013':
        tempe_crispy += barang_terjual
        
    # Terong Crispy Online (GO FOOD)
    elif sku == '70000033':
        terong_crispy += barang_terjual
        
    # Topping Crisbar Online (GO FOOD)
    elif sku == '90000103':
        topping_crisbar += barang_terjual
        
    # Topping Goang Online (GO FOOD)
    elif sku == '90000703':
        topping_goang += barang_terjual
        
    # Topping Keju Online (GO FOOD)
    elif sku == '90000503':
        topping_keju += barang_terjual
        
    # Topping Mamah Online (GO FOOD)
    elif sku == '90000303':
        topping_mamah += barang_terjual
        
    # Topping Manis Online (GO FOOD)
    elif sku == '90000603':
        topping_manis += barang_terjual
        
    # Topping Matah Online (GO FOOD)
    elif sku == '90000203':
        topping_matah += barang_terjual
        
    # Topping Tomat Online (GO FOOD)
    elif sku == '90000403':
        topping_tomat += barang_terjual
        
    # 2 Ayam Crisbar + 3 Ayam Sambal Mix (GRABFOOD)
    elif sku == '10310204':    
        ayam_crispy += barang_terjual
        paper_cost_takeaway_m += 5*barang_terjual
        topping_crisbar += 2*barang_terjual
        topping_matah += barang_terjual
        topping_mamah += barang_terjual
        topping_tomat += barang_terjual
        
    # 3 Ayam Crisbar + 3 Nasi + 3 Es Teh (GRABFOOD)
    elif sku == '10311094':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        topping_crisbar += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        es_teh_takeaway += 3*barang_terjual
        
    # Crisbar + Es Teh + Gratis 2 Kulit (GRABFOOD)
    elif sku == '10611194':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        
    # (Driver)Paket Crispy Es Teh Manis + Lalab (GRABFOOD)
    elif sku == '10711094':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        lalab += barang_terjual
        
    # 3 Ayam Crisbar + 3 Nasi + 3 LemonTea/Lemonade (GRABFOOD)
    elif sku == '10311164':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        topping_crisbar += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        lemon_tea_takeaway += 3*barang_terjual
        
    # 3 Ayam Crisbar + 3 Nasi + 3 Milo (GRABFOOD)
    elif sku == '10311174':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        topping_crisbar += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        milo_takeaway += 3*barang_terjual
        
    # 3 Ayam Crisbar + 3 Nasi + 3 Orange (GRABFOOD)
    elif sku == '10311184':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        topping_crisbar += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        orange_takeaway += 3*barang_terjual
        
    # 3 Ayam Crispy + 3 Nasi + 3 Es Teh (GRABFOOD) + 3 Pudding
    elif sku == '10211894':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        es_teh_takeaway += 3*barang_terjual
        puding_milo_dino += 3*barang_terjual
        
    # 3 Ayam Crispy + 3 Nasi + 3 LemonTea/Lemonade (GRABFOOD)
    elif sku == '10311064':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        lemon_tea_takeaway += 3*barang_terjual
        
    # 3 Ayam Crispy + 3 Nasi + 3 Milo (GRABFOOD)
    elif sku == '10311074':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        milo_takeaway += 3*barang_terjual
        
    # 3 Ayam Crispy + 3 Nasi + 3 Orange (GRABFOOD)
    elif sku == '10311084':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        orange_takeaway += 3*barang_terjual
        
    # 3 Kol Crispy Online (GRABFOOD)
    elif sku == '70000104':
        kol_crispy += 3*barang_terjual
        
    # 4 Ayam Crisbar Original/Geprek Ala Carte (GRABFOOD)
    elif sku == '10310104':
        paper_cost_takeaway_m += 4*barang_terjual
        ayam_geprek_crispy += 4*barang_terjual
        topping_crisbar += 4*topping_crisbar
        
    # 4 Ayam Crispy Original/Geprek Ala Carte (GRABFOOD)
    elif sku == '10310004':
        paper_cost_takeaway_m += 4*barang_terjual
        ayam_geprek_crispy += 4*barang_terjual
        
    # Ayam Crisbar Online (GRABFOOD)
    elif sku == '10011104':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += topping_crisbar
        
    # Ayam Crispy Geprek Online (GRABFOOD)
    elif sku == '10011004':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        
    # Ayam Goang Online (GRABFOOD)
    elif sku == '10011704':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        
    # Ayam Keju Online (GRABFOOD)
    elif sku == '10011504':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
    
    # Ayam Mamah Online (GRABFOOD)
    elif sku == '10011304':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        
    # Ayam Manis Online (GRABFOOD)
    elif sku == '10011604':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        
    # Ayam Matah Online (GRABFOOD)
    elif sku == '10011204':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        
    # Ayam Tomat Online (GRABFOOD)
    elif sku == '10011404':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        
    # Chiken Skin Crispy Online (GRABFOOD)
    elif sku == '70000054':
        dua_chicken_skin_crispy += barang_terjual
        
    # Crisbar + Es Teh + 1 Porsi Kol Crispy (GRABFOOD)
    elif sku == '10611494':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        kol_crispy += barang_terjual
        
    # Crisbar + Es Teh + 2 Kulit + Gratis Pudding (GRABFOOD)
    elif sku == '10311494':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        puding_milo_dino += barang_terjual
        
    # Crisbar + Es Teh + Gratis Tahu dan Tempe (GRABFOOD)
    elif sku == '10611294':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        
    # Crisbar + Es Teh + Tahu dan Tempe + Gratis Pudding (GRABFOOD)
    elif sku == '10311594':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        puding_milo_dino += barang_terjual
        
    # Crisbar + Lemontea/Lemonade + Gratis Tahu dan Tempe (GRABFOOD)
    elif sku == '10611264':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        
    # Crisbar + Lemontea/Lemonade + Tahu dan Tempe + Gratis Pudding (GRABFOOD)
    elif sku == '10311564':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        puding_milo_dino += barang_terjual
        
    # Crisbar + LemoTea/Lemonade + 1 Porsi Kol Crispy (GRABFOOD)
    elif sku == '10611464':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        kol_crispy += barang_terjual
        
    # Crisbar + LemoTea/Lemonade + 2 Kulit + Gratis Pudding (GRABFOOD)
    elif sku == '10311464':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        puding_milo_dino += barang_terjual
        
    # Crisbar + LemoTea/Lemonade + Gratis 2 Kulit (GRABFOOD)
    elif sku == '10611164':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Crisbar + Milo + 1 Porsi Kol Crispy (GRABFOOD)
    elif sku == '10611474':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        kol_crispy += barang_terjual
        
    # Crisbar + Milo + 2 Kulit + Gratis Pudding (GRABFOOD)
    elif sku == '10311474':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        puding_milo_dino += barang_terjual
        
    # Crisbar + Milo + Gratis 2 Kulit (GRABFOOD)
    elif sku == '10611174':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Crisbar + Milo + Gratis Tahu dan Tempe (GRABFOOD)
    elif sku == '10611274':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        milo_takeaway += barang_terjual
        
    # Crisbar + Milo + Tahu dan Tempe + Gratis Pudding (GRABFOOD)
    elif sku == '10311574':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        milo_takeaway += barang_terjual
        puding_milo_dino += barang_terjual
        
    # Crisbar + Orange + 1 Porsi Kol Crispy (GRABFOOD)
    elif sku == '10611484':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        kol_crispy += barang_terjual
        
    # Crisbar + Orange + 2 Kulit + Gratis Pudding (GRABFOOD)
    elif sku == '10311484':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        puding_milo_dino += barang_terjual
        
    # Crisbar + Orange + Gratis 2 Kulit (GRABFOOD)
    elif sku == '10611184':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Crisbar + Orange + Gratis Tahu dan Tempe (GRABFOOD)
    elif sku == '10611284':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        orange_takeaway += barang_terjual
        
    # Crisbar + Orange + Tahu dan Tempe + Gratis Pudding (GRABFOOD)
    elif sku == '10311584':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        orange_takeaway += barang_terjual
        puding_milo_dino += barang_terjual
        
    # Crisbar + Sjora + 2 Kulit + Gratis Pudding (GRABFOOD)
    elif sku == '10311444':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        puding_milo_dino += barang_terjual
        sjora_mango_peach += barang_terjual
        
    # Crisbar + Sjora + Gratis 2 Kulit Chiken Skin (GRABFOOD)
    elif sku == '10611144':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        sjora_mango_peach += barang_terjual
        
    # Crisbar + Sjora + Gratis Tahu dan Tempe (GRABFOOD)
    elif sku == '10611244':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        sjora_mango_peach += barang_terjual
        
    # Crisbar + Sjora + Tahu dan Tempe + Gratis Pudiing (GRABFOOD)
    elif sku == '10311544':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        puding_milo_dino += barang_terjual
        sjora_mango_peach += barang_terjual
        
    # Crispy + Es Teh + 2 Kulit + Gratis Pudding (GRABFOOD)
    elif sku == '10311994':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        puding_milo_dino += barang_terjual
        
    # Crispy + Es Teh + Gratis 2 Kulit (GRABFOOD)
    elif sku == '10611094':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Crispy + LemonTea/Lemonade + Gratis 2 Kulit (GRABFOOD)
    elif sku == '10611064':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Crispy + Milo + Gratis 2 Kulit (GRABFOOD)
    elif sku == '10611074':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Crispy + Orange + Gratis 2 Kulit (GRABFOOD)
    elif sku == '10611084':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    # Es Teh Manis Online (GRABFOOD)
    elif sku == '80000094':
        es_teh_takeaway += barang_terjual
        
    # Free Promo But 1 Get 1 Nikmat Crispy (GRABFOOD)
    elif sku == '10911014':
        paper_cost_takeaway_m += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        
    # Frozen Ayam Crisbar (GRABFOOD)
    elif sku == '1031114':
        packaging_frozen += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        
    # Frozen Ayam Sambal Mamah (GRABFOOD)
    elif sku == '1031134':
        packaging_frozen += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        
    # Kerupuk Online (GRABFOOD)
    elif sku == '70000084':
        kerupuk += barang_terjual
        
    # Lemon Tea Online (GRABFOOD)
    elif sku == '80000064':
        lemon_tea_takeaway += barang_terjual
        
    # Lemonade Online (GRABFOOD)
    elif sku == '80000054':
        lemonade_takeaway += barang_terjual
        
    # Milo Online (GRABFOOD)
    elif sku == '80000074':
        milo_takeaway += barang_terjual
        
    # Nasi Ayam Crisbar (GRABFOOD)
    elif sku == '10111104':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Crispy (GRABFOOD)
    elif sku == '10111004':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Goang (GRABFOOD)
    elif sku == '10111704':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Keju (GRABFOOD)
    elif sku == '10111504':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Mamah (GRABFOOD)
    elif sku == '10111304':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Manis (GRABFOOD)
    elif sku == '10111604':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Matah (GRABFOOD)
    elif sku == '10111204':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Ayam Tomat (GRABFOOD)
    elif sku == '10111404':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        
    # Nasi Online (GRABFOOD)
    elif sku == '70000004':
        nasi_takeaway += barang_terjual
        
    # Orange Onlien (GRABFOOD)
    elif sku == '80000084':
        orange_takeaway += barang_terjual
        
    # P.Crisbar+P.Keju+2 Es Teh+Gratis 2 Tempe 4 Kulit (GRABFOOD)
    elif sku == '10611394':
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += 2*barang_terjual
        es_teh_takeaway += 2*barang_terjual
        tempe_crispy += 2*barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        
    # P.Crisbar+P.Keju+2 LemonTea/Lemonade+Gratis 2 Tempe 4 Kulit (GRABFOOD)
    elif sku == '10211090':
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += 2*barang_terjual
        lemon_tea_takeaway += 2*barang_terjual
        tempe_crispy += 2*barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual

    # P.Crisbar+P.Keju+2 Milo+Gratis 2 Tempe 2 Kulit (GRABFOOD)
    elif sku == '10611374':
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += 2*barang_terjual
        milo_takeaway += 2*barang_terjual
        tempe_crispy += 2*barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # P.Crisbar+P.Keju+2 Orange+Gratis 2 Tempe 2 Kulit (GRABFOOD)
    elif sku == '10611384':
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += 2*barang_terjual
        orange_takeaway += 2*barang_terjual
        tempe_crispy += 2*barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Paket 4 Chiken Skin + Es Teh Online (GRABFOOD)
    elif sku == '10200194':
        paper_cost_takeaway_l += barang_terjual
        nasi_takeaway += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket 4 Chiken Skin + Lemon Online (GRABFOOD)
    elif sku == '10200164':
        paper_cost_takeaway_l += barang_terjual
        nasi_takeaway += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket 4 Chiken Skin + Milo Online (GRABFOOD)
    elif sku == '10200174':
        paper_cost_takeaway_l += barang_terjual
        nasi_takeaway += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        milo_takeaway += barang_terjual

    # Paket 4 Chiken Skin + Orange Online (GRABFOOD)
    elif sku == '10200184':
        paper_cost_takeaway_l += barang_terjual
        nasi_takeaway += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Crisbar Bumbu Bali + Es Teh (GRABFOOD)
    elif sku == '10912394':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        topping_crisbar += barang_terjual
        topping_matah += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Crisbar Es Teh Online (GRABFOOD)
    elif sku == '10111194':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        topping_crisbar += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Crisbar LemonTea/Lemonade Online (GRABFOOD)
    elif sku == '10111164':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        topping_crisbar += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Crisbar Milo Online (GRABFOOD)
    elif sku == '10111174':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        topping_crisbar += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Crisbar Orange Online (GRABFOOD)
    elif sku == '10111184':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        topping_crisbar += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Crispy Es Teh Online (GRABFOOD)
    elif sku == '10111094':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Crispy Lemon Tea/Lemonade Online (GRABFOOD)
    elif sku == '10111064':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Crispy Milo Online (GRABFOOD)
    elif sku == '10111074':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        topping_crisbar += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Crispy Orange Online (GRABFOOD)
    elif sku == '10111084':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual


    # Paket Ayam Goang Es Teh Online (GRABFOOD)
    elif sku == '10111794':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Goang LemonTea/Lemonade Online (GRABFOOD)
    elif sku == '10111764':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Goang Milo Online (GRABFOOD)
    elif sku == '10111774':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Goang Orange Online (GRABFOOD)
    elif sku == '10111784':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Keju Es Teh Online (GRABFOOD)
    elif sku == '10111594':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Keju Lemon Tea/Lemonade Online (GRABFOOD)
    elif sku == '10111564':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Keju Milo Online (GRABFOOD)
    elif sku == '10111574':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Keju Orange Online (GRABFOOD)
    elif sku == '10111584':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Mamah Es Teh Online (GRABFOOD)
    elif sku == '10111394':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Mamah Lemon Tea/Lemonade Online (GRABFOOD)
    elif sku == '10111364':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Mamah Milo Online (GRABFOOD)
    elif sku == '10111374':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Mamah Orange Online (GRABFOOD)
    elif sku == '10111384':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Manis Es Teh Online (GRABFOOD)
    elif sku == '10111694':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Manis Lemon Tea/Lemonade Online (GRABFOOD)
    elif sku == '10111664':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Manis Milo Online (GRABFOOD)
    elif sku == '10111674':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Manis Orange Online (GRABFOOD)
    elif sku == '10111684':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Matah Es Teh Online (GRABFOOD)
    elif sku == '10111294':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Matah Lemon Tea/Lemonade Online (GRABFOOD)
    elif sku == '10111264':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Matah Milo Online (GRABFOOD)
    elif sku == '10111274':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Matah Orange Online (GRABFOOD)
    elif sku == '10111284':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Tomat Es Teh Online (GRABFOOD)
    elif sku == '10111494':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Tomat LemonTea/Lemonade Online (GRABFOOD)
    elif sku == '10111464':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Tomat Milo Online (GRABFOOD)
    elif sku == '10111474':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Tomat Orange Online (GRABFOOD)
    elif sku == '10111484':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Crisbar Madu Es Teh Online (GRABFOOD)
    elif sku == '10111993':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar_madu += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Side Dish Es Teh Online (GRABFOOD)
    elif sku == '10200294':
        paper_cost_takeaway_l += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Side Dish Lemon Online (GRABFOOD) 
    elif sku == '10200264':
        paper_cost_takeaway_l += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Side Dish Milo Online (GRABFOOD)
    elif sku == '10200274':
        paper_cost_takeaway_l += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Side Dish Milo Online (GRABFOOD)
    elif sku == '10200284':
        paper_cost_takeaway_l += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Promo Ayam Crisbar+Ayam Keju+2 Nasi+2 Es Teh+2 Tempe+4 Kulit (GRABFOOD)
    elif sku == '10910194':
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += 2*barang_terjual
        es_teh_takeaway += 2*barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        
    # Crisbar + Nasi + Es Teh + 2 Chiken Skin + Tote Bag (GRABFOOD)
    elif sku == '10911094':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Promo Ayam Geprek Keju + Nasi + Es Teh + 2 Chiken Skin (GRABFOOD)
    elif sku == '10911594':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Promo Ayam Geprek Manis + Nasi + Es Teh + 2 Chiken Skin (GRABFOOD)
    elif sku == '10911694':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Promo Ayam Keju+Ayam Crispy+2 Nasi+2 Es Teh+2 Terong+4 Kulit (GRABFOOD)
    elif sku == '10910594':
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += 2*barang_terjual
        es_teh_takeaway += 2*barang_terjual
        terong_crispy += 2*barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual

    # Promo Ayam Manis+Ayam Crispy+2 Nasi+2 Es Teh+2 Tahu+4 Kulit (GRABFOOD)
    elif sku == '10910694':
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += 2*barang_terjual
        es_teh_takeaway += 2*barang_terjual
        tahu_crispy += 2*barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual

    # Promo Paket Nasi Kulit Chiken Skin + Minum (GRABFOOD)
    elif sku == '10900194':
        paper_cost_takeaway_l += barang_terjual
        nasi_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        es_teh_takeaway += barang_terjual

    # Promo Paket Nasi Telur Tahu Tempe + Minum (GRABFOOD)
    elif sku == '10900294':
        paper_cost_takeaway_l += barang_terjual
        nasi_takeaway += barang_terjual
        telur_sayur += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        es_teh_takeaway += barang_terjual

    # Pudding Milo Dino Online (GRABFOOD)
    elif sku == '50000024':
        puding_milo_dino += barang_terjual

    # Raksasa Crisbar + Tahu + Tempe + Terong + Telur + Kulit+ Milo (GRABFOOD)
    elif sku == '10211074':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Crisbar + Tahu + Tempe + Terong+ Telur + Kulit+ Es Teh (GRABFOOD)
    elif sku == '10211094':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Crisbar + Tahu + Tempe + Terong+ Telur + Kulit+ Lemon (GRABFOOD)
    elif sku == '10211064':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Crisbar + Tahu + Tempe + Terong+ Telur + Kulit+ Orange (GRABFOOD)
    elif sku == '10211084':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Crispy + Tahu + Tempe + Terong + Telur + Kulit+ Milo (GRABFOOD)
    elif sku == '10211174':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Crispy + Tahu + Tempe + Terong+ Telur + Kulit+ Es Teh (GRABFOOD)
    elif sku == '10211194':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Crispy + Tahu + Tempe + Terong+ Telur + Kulit+ Lemon (GRABFOOD)
    elif sku == '10211164':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Crispy + Tahu + Tempe + Terong+ Telur + Kulit+ Orange (GRABFOOD)
    elif sku == '10211184':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Keju + Tahu + Tempe + Terong+ Telur + Kulit+ Es Teh (GRABFOOD)
    elif sku == '10211394':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Keju + Tahu + Tempe + Terong+ Telur + Kulit+ Lemon (GRABFOOD)
    elif sku == '10211364':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Keju + Tahu + Tempe + Terong+ Telur + Kulit+ Milo (GRABFOOD)
    elif sku == '10211374':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Keju + Tahu + Tempe + Terong+ Telur + Kulit+ Orange (GRABFOOD)
    elif sku == '10211384':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Manis + Tahu + Tempe + Terong + Telur + Kulit+ Es Teh (GRABFOOD)
    elif sku == '10211294':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Manis + Tahu + Tempe + Terong + Telur + Kulit+ Lemon (GRABFOOD)
    elif sku == '10211264':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Manis + Tahu + Tempe + Terong + Telur + Kulit+ Milo
    elif sku == '10211274':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Raksasa Manis + Tahu + Tempe + Terong + Telur + Kulit+ Orange (GRABFOOD)
    elif sku == '10211284':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Sjora Mango Peach Online (GRABFOOD)
    elif sku == '80000044':
        sjora_mango_peach += barang_terjual

    # Tahu Crispy Online (GRABFOOD)
    elif sku == '70000024':
        tahu_crispy += barang_terjual

    # Telur Sayur Online (GRABFOOD)
    elif sku == '70000044':
        telur_sayur += barang_terjual

    # Tempe Crispy Online (GRABFOOD)
    elif sku == '70000014':
        tempe_crispy += barang_terjual

    # Terong Crispy Online (GRABFOOD)
    elif sku == '70000034':
        terong_crispy += barang_terjual

    # Topping Crisbar Online (GRABFOOD)
    elif sku == '90000104':
        topping_crisbar += barang_terjual

    # Topping Goang Online (GRABFOOD)
    elif sku == '90000704':
        topping_goang += barang_terjual

    # Topping Keju Online (GRABFOOD)
    elif sku == '90000504':
        topping_keju += barang_terjual

    # Topping Mamah Online (GRABFOOD)
    elif sku == '90000304':
        topping_mamah += barang_terjual

    # Topping Manis Online (GRABFOOD)
    elif sku == '90000604':
        topping_manis += barang_terjual

    # Topping Matah Online (GRABFOOD)
    elif sku == '90000204':
        topping_mamah_frozen += barang_terjual

    # Topping Tomat Online (GRABFOOD)
    elif sku == '90000404':
        topping_tomat += barang_terjual

    # (Crew)Nasi + 2 Chiken Skin + Topping Manis + 1 Cup Es Teh (GRABFOOD)
    elif sku == '10200690':
        paper_cost_dine_in += barang_terjual
        topping_manis += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # (Crew)Nasi + Tahu Crispy + Terong + Topping Matah + 1 Cup Es Teh
    elif sku == '10200590':
        paper_cost_dine_in += barang_terjual
        topping_matah += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual
        tahu_crispy += barang_terjual

    # (Crew)Nasi + Telur + Tempe Crispy + Topping Goang + 1 Cup Es Teh
    elif sku == '10200490':
        paper_cost_dine_in += barang_terjual
        telur_sayur += barang_terjual
        tempe_crispy += barang_terjual
        topping_goang += barang_terjual
        es_teh_dine_in += barang_terjual

    # Paket Crisbar + Terong Crispy + Es Teh Manis (SURPLUS)
    elif sku == '10005':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        terong_crispy += barang_terjual
        es_teh_dine_in += barang_terjual

    # Paket Sambal Tomat + Tempe Crispy + Es Teh Manis (SURPLUS)
    elif sku == '10006':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        tempe_crispy += barang_terjual
        es_teh_dine_in += barang_terjual

    # 2 Ayam Crisbar + 3 Ayam Sambal Mix (TAKE AWAY)
    elif sku == '10310202':
        ayam_crispy += 5*barang_terjual
        paper_cost_takeaway_m += 5*barang_terjual
        topping_crisbar += 2*barang_terjual
        topping_matah += barang_terjual
        topping_mamah += barang_terjual
        topping_tomat += barang_terjual

    # 3 Ayam Crisbar + 3 Nasi + 3 Es Teh Take Away (TAKE AWAY)
    elif sku == '10311192':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        topping_crisbar += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        es_teh_takeaway += 3*barang_terjual

    # 3 Ayam Crispy+ 3 Nasi + 3 Es Teh Take Away (TAKE AWAY)
    elif sku == '10311092':
        paper_cost_takeaway_l += 3*barang_terjual
        ayam_geprek_crispy += 3*barang_terjual
        nasi_takeaway += 3*barang_terjual
        es_teh_takeaway += 3*barang_terjual

    # 3 Kol Crispy Take Away (TAKE AWAY)
    elif sku == '70000102':
        kol_crispy += 3*barang_terjual

    # 4 Ayam Crisbar Original/Geprek Ala Carte (TAKE AWAY)
    elif sku == '10310102':
        paper_cost_takeaway_m += 4*barang_terjual
        ayam_geprek_crispy += 4*barang_terjual
        topping_crisbar += 4*topping_crisbar

    # 4 Ayam Crispy Original/Geprek Ala Carte (TAKE AWAY)
    elif sku == '10310002':
        paper_cost_takeaway_m += 4*barang_terjual
        ayam_geprek_crispy += 4*barang_terjual

    # Ayam Crisbar Take Away (TAKE AWAY)
    elif sku == '10011102':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual

    # Ayam Crispy Geprek Take Away (TAKE AWAY)
    elif sku == '10011002':
        paper_cost_takeaway_m += barang_terjual
        ayam_geprek_crispy += barang_terjual

    # Ayam Crispy Take Away (TAKE AWAY)
    elif sku == '10010002':
        ayam_crispy += barang_terjual
        paper_cost_takeaway_m += barang_terjual

    # Ayam Goang Take Away (TAKE AWAY)
    elif sku == '10011702':
        paper_cost_takeaway_m += barang_terjual
        ayam_crispy += barang_terjual
        topping_goang += barang_terjual

    # Ayam Keju Take Away (TAKE AWAY)
    elif sku == '10011502':
        paper_cost_takeaway_m += barang_terjual
        ayam_crispy += barang_terjual
        topping_keju += barang_terjual

    # Ayam Mamah Take Away (TAKE AWAY)
    elif sku == '10011302':
        paper_cost_takeaway_m += barang_terjual
        ayam_crispy += barang_terjual
        topping_mamah += barang_terjual

    # Ayam Manis Take Away (TAKE AWAY)
    elif sku == '10011602':
        paper_cost_takeaway_m += barang_terjual
        ayam_crispy += barang_terjual
        topping_manis += barang_terjual

    # Ayam Matah Take Away (TAKE AWAY)
    elif sku == '10011202':
        paper_cost_takeaway_m += barang_terjual
        ayam_crispy += barang_terjual
        topping_manis += barang_terjual

    # Ayam Saos BBQ Cheese Take Away (TAKE AWAY)
    elif sku == '1001212':
        ayam_crispy += barang_terjual
        paper_cost_takeaway_m += barang_terjual
        topping_bbq_cheese += barang_terjual

    # Ayam Saos BBQ Cheese Take Away (TAKE AWAY)
    elif sku == '10012102':
        ayam_crispy += barang_terjual
        paper_cost_takeaway_m += barang_terjual
        topping_bbq_cheese += barang_terjual

    # Ayam Saos Gravy Take Away (TAKE AWAY)
    elif sku == '10012202':
        ayam_crispy += barang_terjual
        paper_cost_takeaway_m += barang_terjual
        topping_bbq_gravy += barang_terjual

    # Ayam Saos Gravy Take Away (TAKE AWAY)
    elif sku == '1001222':
        ayam_crispy += barang_terjual
        paper_cost_takeaway_m += barang_terjual
        topping_bbq_gravy += barang_terjual

    # Ayam Tomat Take Away (TAKE AWAY)
    elif sku == '10011402':
        ayam_crispy += barang_terjual
        paper_cost_takeaway_m += barang_terjual
        topping_tomat += barang_terjual

    # Chiken Skin Crispy Take Away (TAKE AWAY)
    elif sku == '70000052':
        dua_chicken_skin_crispy += barang_terjual

    # Crisbar + Es Teh + 1 Porsi Kol Crispy Take Away (TAKE AWAY)
    elif sku == '10611492':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        kol_crispy += barang_terjual

    # Crisbar + Es Teh + Gratis 2 Kulit Take Away (TAKE AWAY)
    elif sku == '10611192':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Crisbar + Es Teh + Gratis Tahu dan Tempe Take Away (TAKE AWAY)
    elif sku == '10611292':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual

    # Crisbar + Lemontea/Lemonade + Gratis Tahu dan Tempe Take Away (TAKE AWAY)
    elif sku == '10611262':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Crisbar + LemoTea/Lemonade + 1 Porsi Kol Crispy Take Away (TAKE AWAY)
    elif sku == '10611462':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
        kol_crispy += barang_terjual

    # Crisbar + LemoTea/Lemonade + Gratis 2 Kulit Take Away (TAKE AWAY)
    elif sku == '10611162':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Crisbar + Milo + 1 Porsi Kol Crispy Take Away (TAKE AWAY)
    elif sku == '10611472':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
        kol_crispy += barang_terjual

    # Crisbar + Milo + Gratis 2 Kulit Take Away (TAKE AWAY)
    elif sku == '10611172':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Crisbar + Milo + Gratis Tahu dan Tempe Take Away (TAKE AWAY)
    elif sku == '10611272':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        milo_takeaway += barang_terjual

    # Crisbar + Orange + 1 Porsi Kol Crispy Take Away (TAKE AWAY)
    elif sku == '10611482':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        kol_crispy += barang_terjual

    # Crisbar + Orange + Gratis 2 Kulit Take Away (TAKE AWAY)
    elif sku == '10611182':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Crisbar + Orange + Gratis Tahu dan Tempe Take Away (TAKE AWAY)
    elif sku == '10611282':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual

    # Crispy + Es Teh + Gratis 2 Kulit Take Away (TAKE AWAY)
    elif sku == '10611092':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Crispy + LemonTea/Lemonade + Gratis 2 Kulit Take Away (TAKE AWAY)
    elif sku == '10611062':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Crispy + Milo + Gratis 2 Kulit Take Away (TAKE AWAY)
    elif sku == '10611072':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
    
    # Crispy + Orange + Gratis 2 Kulit Take Away (TAKE AWAY)
    elif sku == '10611082':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
    
    # Es Teh Manis Take Away (TAKE AWAY)
    elif sku == '80000092':
        es_teh_takeaway += barang_terjual
    
    # Kotak Packaging L (TAKE AWAY)
    elif sku == '20010000':
        paper_cost_takeaway_l += barang_terjual
    
    # Kotak Packaging M (TAKE AWAY)
    elif sku == '20011000':
        paper_cost_takeaway_m += barang_terjual
    
    # Kuah Tongseng Take Away (TAKE AWAY)
    elif sku == '70000062':
        kuah_tongseng += barang_terjual
    
    # Lemon Tea Takeaway (TAKE AWAY)
    elif sku == '80000062':
        lemon_tea_takeaway += barang_terjual

    # Lemonade Take Away (TAKE AWAY)
    elif sku == 'Lemonade Take Away':
        lemonade_takeaway += barang_terjual

    # Milo Takeaway (TAKE AWAY)
    elif sku == '80000072':
        milo_takeaway += barang_terjual

    # Nasi Takeaway (TAKE AWAY)
    elif sku == '70000002':
        nasi_takeaway += barang_terjual

    # Nugget Take Away (TAKE AWAY)
    elif sku == '70000072':
        nugget += barang_terjual
    
    # Orange Take Away (TAKE AWAY)
    elif sku == '80000082':
        orange_takeaway += barang_terjual
    
    # Paket 4 Chiken Skin + Es Teh Take Away (TAKE AWAY)
    elif sku == '10200192':
        paper_cost_takeaway_l += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
    
    # Paket 4 Chiken Skin + Lemon Take Away (TAKE AWAY)
    elif sku == '10200162':
        paper_cost_takeaway_l += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual
    
    # Paket 4 Chiken Skin + Milo Take Away (TAKE AWAY)
    elif sku == '10200172':
        paper_cost_takeaway_l += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual
    
    # Paket 4 Chiken Skin + Orange Take Away (TAKE AWAY)
    elif sku == '10200182':
        paper_cost_takeaway_l += barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual
    
    # Paket Ayam Crisbar Es Teh Take Away (TAKE AWAY)
    elif sku == '10111192':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual
    
    # Paket Ayam Crisbar Lemontea/Lemonade Take Away (TAKE AWAY)
    elif sku == '10111162':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Crisbar Milo Take Away (TAKE AWAY)
    elif sku == '10111172':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Crisbar Orange Take Away (TAKE AWAY)
    elif sku == '10111182':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Crispy Es Teh Take Away (TAKE AWAY)
    elif sku == '10110092':
        paper_cost_takeaway_l += barang_terjual
        ayam_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Crispy Milo Take Away (TAKE AWAY)
    elif sku == '10110072':
        paper_cost_takeaway_l += barang_terjual
        ayam_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Crispy Orange Take Away (TAKE AWAY)
    elif sku == '10110082':
        paper_cost_takeaway_l += barang_terjual
        ayam_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Geprek Crispy Es Teh Take Away(TAKE AWAY)
    elif sku == '10111092':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Geprek Crispy Lemontea/Lemonade Take Away (TAKE AWAY)
    elif sku == '10111062':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Geprek Crispy Milo Take Away (TAKE AWAY)
    elif sku == '10111072':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Geprek Crispy Orange Take Away (TAKE AWAY)
    elif sku == '10111082':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Goang Es Teh Take Away (TAKE AWAY)
    elif sku == '10111792':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Goang Lemontea/Lemonade Take Away (TAKE AWAY)
    elif sku == '10111762':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Goang Milo Take Away (TAKE AWAY)
    elif sku == '10111772':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Goang Orange Take Away (TAKE AWAY)
    elif sku == '10111782':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_goang += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Keju Es Teh Take Away (TAKE AWAY)
    elif sku == '10111592':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Keju Lemontea/Lemonade Take Away (TAKE AWAY)
    elif sku == '10111562':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Keju Milo Take Away (TAKE AWAY)
    elif sku == '10111572':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Keju Orange Take Away (TAKE AWAY)
    elif sku == '10111582':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_keju += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Mamah Es Teh Take Away (TAKE AWAY)
    elif sku == '10111392':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Mamah Lemontea/Lemonade Take Away (TAKE AWAY)
    elif sku == '10111362':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Mamah Milo Take Away (TAKE AWAY)
    elif sku == '10111372':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Mamah Orange Take Away (TAKE AWAY)
    elif sku == '10111382':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_mamah += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Manis Es Teh Take Away (TAKE AWAY)
    elif sku == '10111692':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Manis Lemontea/Lemonade Take Away (TAKE AWAY)
    elif sku == '10111662':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Manis Milo Take Away (TAKE AWAY)
    elif sku == '10111672':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Manis Orange Take Away (TAKE AWAY)
    elif sku == '10111682':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_manis += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Matah Es Teh Take Away (TAKE AWAY)
    elif sku == '10111292':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Matah Lemontea/Lemonade Take Away (TAKE AWAY)
    elif sku == '10111262':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Matah Milo Take Away (TAKE AWAY)
    elif sku == '10111272':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Matah Orange Take Away (TAKE AWAY)
    elif sku == '10111282':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Saos  BBQ Cheese Orange Take Away (TAKE AWAY)
    elif sku == '10112182':
        ayam_crispy += barang_terjual
        paper_cost_takeaway_l += barang_terjual
        topping_bbq_cheese += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Saos BBQ Cheese Es Teh Take Away (TAKE AWAY)
    elif sku == '10112192':
        ayam_crispy += barang_terjual
        paper_cost_takeaway_l += barang_terjual
        topping_bbq_cheese += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Saos BBQ Cheese Milo Take Away (TAKE AWAY)
    elif sku == '10112172':
        ayam_crispy += barang_terjual
        paper_cost_takeaway_l += barang_terjual
        topping_bbq_cheese += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Saos Gravy Es Teh Take Away (TAKE AWAY)
    elif sku == '10112292':
        ayam_crispy += barang_terjual
        paper_cost_takeaway_l += barang_terjual
        topping_bbq_gravy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Saos Gravy Milo Take Away (TAKE AWAY)
    elif sku == '10112272':
        ayam_crispy += barang_terjual
        paper_cost_takeaway_l += barang_terjual
        topping_bbq_gravy += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Saos Gravy Orange Take Away (TAKE AWAY)
    elif sku == '10112282':
        ayam_crispy += barang_terjual
        paper_cost_takeaway_l += barang_terjual
        topping_bbq_gravy += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Ayam Tomat Es Teh Take Away (TAKE AWAY)
    elif sku == '10111492':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Tomat Lemontea/Lemonade Take Away (TAKE AWAY)
    elif sku == '10111462':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Tomat Milo Take Away (TAKE AWAY)
    elif sku == '10111472':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Tomat Orange Take Away (TAKE AWAY)
    elif sku == '10111482':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_tomat += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paket Side Dish Es Teh Take Away (TAKE AWAY)
    elif sku == '10200292':
        paper_cost_takeaway_l += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Side Dish Lemon Take Away (TAKE AWAY)
    elif sku == '10200262':
        paper_cost_takeaway_l += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Side Dish Milo Take Away (TAKE AWAY)
    elif sku == '10200272':
        paper_cost_takeaway_l += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Side Dish Orange Take Away (TAKE AWAY)
    elif sku == '10200282':
        paper_cost_takeaway_l += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        telur_sayur += barang_terjual
        nasi_takeaway += barang_terjual
        orange_takeaway += barang_terjual

    # Paperbag (TAKE AWAY)
    elif sku == '20012000':
        paper_cost_takeaway_paper_bag += barang_terjual

    # Rakasa Crispy+Tahu+Tempe+Terong+Telur+Kulit+Es Teh Take Away (TAKE AWAY)
    elif sku == '10211192':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Raksasa Crisbar+Tahu+Tempe+Terong+Telur+Kulit+Es Teh Take Away (TAKE AWAY)
    elif sku == '10211092':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual     
        tahu_crispy += barang_terjual
        tempe_crispy += barang_terjual
        terong_crispy += barang_terjual
        telur_sayur += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # YANG BARUUUUUUUUUUUUUUUUU
    # 2 Ayam Crisbar + 2 Nasi + 2 Es Teh + Tote Bag/Tumbler (DINE IN)
    elif (sku == '10911290') or (sku == '10911390') :
        paper_cost_dine_in += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += 2*barang_terjual
        nasi_dine_in += 2*barang_terjual
        es_teh_dine_in += 2*barang_terjual

    # 2 Ayam Crisbar + 2 Nasi + 2 Es Teh + Tote Bag/Tumbler (ONLINE/TAKE AWAY)
    elif (sku == '10911292') or (sku == '10911293') or (sku == '10911294') or (sku == '10911392') or (sku == '10911393') or (sku == '10911394'):
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += 2*barang_terjual
        nasi_takeaway += 2*barang_terjual
        es_teh_takeaway += 2*barang_terjual

    # 2 Ayam Crisbar + 2 Nasi + 2 Lemon + Tote Bag (DINE IN)
    elif sku == '10911260':
        paper_cost_dine_in += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += 2*barang_terjual
        nasi_dine_in += 2*barang_terjual
        lemon_tea_dine_in += 2*barang_terjual

    # 2 Ayam Crisbar + 2 Nasi + 2 Lemon + Tote Bag/Tumbler (ONLINE/TAKE AWAY)
    elif (sku == '10911264') or (sku == '10911363') or (sku == '10911364'):
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += 2*barang_terjual
        nasi_takeaway += 2*barang_terjual
        lemon_tea_takeaway += 2*barang_terjual

    # 2 Ayam Crisbar + 2 Nasi + 2 Milo + Tote Bag/Tumbler (ONLINE/TAKE AWAY)
    elif (sku == '10911273') or (sku == '10911274') or (sku == '10911373') or (sku == '10911374'):
        paper_cost_takeaway_l += 2*barang_terjual
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += 2*barang_terjual
        nasi_takeaway += 2*barang_terjual
        milo_takeaway += 2*barang_terjual

    # 4 Ayam Crispy Original/Geprek Ala Carte + Tote bag (DINE IN)
    elif sku == '10911400':
        ayam_geprek_crispy += 4*barang_terjual
        paper_cost_dine_in += 4*barang_terjual

    # 4 Ayam Crispy Original/Geprek Ala Carte + Tote bag/Tumbler (ONLINE/TAKE AWAY)
    elif (sku == '10911402') or (sku == '10911404') or (sku == '10911502') or (sku == '10911503') or (sku == '10911504'):
        ayam_geprek_crispy += 4*barang_terjual
        paper_cost_takeaway_m += 4*barang_terjual

    # Ayam Crisbar Matah (DINE IN)
    elif sku == '10910700':
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        topping_matah += barang_terjual
        paper_cost_dine_in += barang_terjual
 
    # Ayam Crisbar Matah Takeaway (TAKE AWAY)
    elif sku == '10910702':
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        topping_matah += barang_terjual
        paper_cost_takeaway_m += barang_terjual

    # Ayam Crisbar Online (GO FOOD)
    elif sku == '10011103':
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        paper_cost_takeaway_m += barang_terjual

    # Ayam Crispy Online / Takeaway (ONLINE/TAKE AWAY)
    elif (sku == '100110041') or (sku == '10010003') or (sku == '10010004') or (sku == '1001002'):
        ayam_crispy += barang_terjual
        paper_cost_takeaway_m += barang_terjual

    # Ayam Keju Online (GRABFOOD)
    elif sku == '1001154':
        ayam_crispy += barang_terjual
        topping_keju += barang_terjual
        paper_cost_takeaway_m += barang_terjual

    # Ayam Matah Online (GO FOOD)
    elif sku == '10011203':
        ayam_crispy += barang_terjual
        topping_matah += barang_terjual
        paper_cost_takeaway_m += barang_terjual

    # Crisbar + Nasi + Es Teh + 2 Chiken Skin + Tote Bag/Tumbler (DINE IN)
    elif (sku == '10911090') or (sku == '10911190'):
        ayam_geprek_crispy += barang_terjual
        paper_cost_dine_in += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        es_teh_dine_in += barang_terjual

    # Crisbar + Nasi + Es Teh + 2 Chiken Skin + Tote Bag/Tumbler (ONLINE/TAKE AWAY)
    elif sku in ['10911092','10911093','10911192','10911193','10911194']:
        ayam_geprek_crispy += barang_terjual
        paper_cost_takeaway_l += barang_terjual
        topping_crisbar += barang_terjual
        nasi_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        es_teh_takeaway += barang_terjual
    
    # Crisbar + Nasi + Lemon + 2 Chiken Skin + Tumbler (DINE IN)
    elif sku == '10911160':
        ayam_geprek_crispy += barang_terjual
        paper_cost_dine_in += barang_terjual
        topping_crisbar += barang_terjual
        nasi_dine_in += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        lemon_tea_dine_in += barang_terjual

    # Crisbar + Nasi + Lemon + 2 Chiken Skin + Tote Bag/Tumbler (ONLINE/TAKE AWAY)
    elif sku in ['10911064', '10911163', '10911164']:
        ayam_geprek_crispy += barang_terjual
        paper_cost_takeaway_l += barang_terjual
        nasi_takeaway += barang_terjual
        topping_crisbar += barang_terjual
        lemon_tea_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Crisbar + Nasi + Orange + 2 Chiken Skin + Tote Bag/Tumbler (ONLINE/TAKE AWAY)
    elif sku in ['10911082', '10911083', '10911084', '10911183', '10911184']:
        ayam_geprek_crispy += barang_terjual
        paper_cost_takeaway_l += barang_terjual
        nasi_takeaway += barang_terjual
        topping_crisbar += barang_terjual
        orange_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Crisbar + Nasi + Milo + 2 Chiken Skin + Tote Bag/Tumbler (ONLINE/TAKE AWAY)
    elif sku in ['10911073', '10911074', '10911173', '10911174']:
        ayam_geprek_crispy += barang_terjual
        paper_cost_takeaway_l += barang_terjual
        nasi_takeaway += barang_terjual
        topping_crisbar += barang_terjual
        milo_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Kresek M atau Kresek S, dan Tumbler
    elif (sku == '20001000') or (sku == '20002000') or (sku == '60000022'):
        continue

    # Lemonade Take Away (TAKE AWAY)
    elif sku == '80000052':
        lemonade_takeaway += barang_terjual

    # Paket Ayam Crisbar Matah Es Teh (DINE IN)
    elif sku == '10910790':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        topping_matah += barang_terjual
        nasi_dine_in += barang_terjual
        es_teh_dine_in += barang_terjual

    # Paket Ayam Crisbar Matah Lemon (DINE IN)
    elif sku == '10910760':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        topping_matah += barang_terjual
        nasi_dine_in += barang_terjual
        lemon_tea_dine_in += barang_terjual

    # Paket Ayam Crisbar Matah Milo (DINE IN)
    elif sku == '10910770':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        topping_matah += barang_terjual
        nasi_dine_in += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Ayam Crisbar Matah Orange (DINE IN)
    elif sku == '10910780':
        paper_cost_dine_in += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        topping_matah += barang_terjual
        nasi_dine_in += barang_terjual
        orange_dine_in += barang_terjual

    # Paket Ayam Crisbar Matah Es Teh Takeaway (TAKE AWAY)
    elif sku == '10910792':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        es_teh_takeaway += barang_terjual

    # Paket Ayam Crisbar Matah Lemon Takeaway (TAKE AWAY)
    elif sku == '10910762':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        lemon_tea_takeaway += barang_terjual

    # Paket Ayam Crisbar Matah Milo Takeaway (TAKE AWAY)
    elif sku == '10910772':
        paper_cost_takeaway_l += barang_terjual
        ayam_geprek_crispy += barang_terjual
        topping_crisbar += barang_terjual
        topping_matah += barang_terjual
        nasi_takeaway += barang_terjual
        milo_takeaway += barang_terjual

    # Paket Crispy Es Teh Manis + Lalab (GRABFOOD)
    elif sku == '10119994':
        ayam_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        paper_cost_takeaway_l += barang_terjual
        es_teh_takeaway += barang_terjual
        lalab += barang_terjual

    # Promo Ayam Geprek Crispy + Nasi + Es Teh + 2 Chiken Skin (GRABFOOD)
    elif sku == '10911794':
        ayam_geprek_crispy += barang_terjual
        nasi_takeaway += barang_terjual
        paper_cost_takeaway_l += barang_terjual
        es_teh_takeaway += barang_terjual
        dua_chicken_skin_crispy += barang_terjual

    # Pudding Milo Dino (TAKE AWAY)
    elif sku == '50000022':
        puding_milo_dino += barang_terjual

    # Tahu Crispy Take Away (TAKE AWAY)
    elif sku == '70000022':
        tahu_crispy += barang_terjual

    # Telur Sayur Take Away (TAKE AWAY)
    elif sku == '70000042':
        telur_sayur += barang_terjual

    # Tempe Crispy Take Away (TAKE AWAY)
    elif sku == '70000012':
        tempe_crispy += barang_terjual

    # Terong Crispy Take Away (TAKE AWAY)
    elif sku == '70000032':
        terong_crispy += barang_terjual

    # Topping Crisbar Take Away (TAKE AWAY)
    elif sku == '90000102':
        topping_crisbar += barang_terjual

    # Topping Goang Take Away (TAKE AWAY)
    elif sku == '90000702':
        topping_goang += barang_terjual

    # Topping Keju Take Away (TAKE AWAY)
    elif sku == '90000502':
        topping_keju += barang_terjual

    # Topping Mamah Online (ONLINE)
    elif (sku == '9000133') or (sku == '9000134'):
        topping_mamah += barang_terjual

    # Topping Mamah Take Away (TAKE AWAY)
    elif sku == '90000302':
        topping_mamah += barang_terjual

    # Topping Manis Take Away (TAKE AWAY)
    elif sku == '90000602':
        topping_manis += barang_terjual

    # Topping Matah Take Away (TAKE AWAY)
    elif (sku == '9000122') or (sku == '90000202'):
        topping_matah += barang_terjual

    # Topping Tomat Take Away (TAKE AWAY)
    elif sku == '90000402':
        topping_tomat += barang_terjual

    # P.Crisbar+P.Keju+2 LemonTea/Lemonade+Gratis 2 Tempe 4 Kulit (GRABFOOD)
    elif sku == '10611364':
        ayam_geprek_crispy += 2*barang_terjual
        paper_cost_takeaway_l += 2*barang_terjual
        topping_crisbar += barang_terjual
        topping_keju += barang_terjual
        lemon_tea_takeaway += 2*barang_terjual
        tempe_crispy += 2*barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual

    # Cheese Berdua, ayam keju, ayam crispy, 2 nasi, 2 minum, 2 terong, 4 chicken skin (DINE IN)
    elif sku == '10910590':
        ayam_geprek_crispy += 2*barang_terjual
        topping_keju += barang_terjual
        paper_cost_dine_in += 2*barang_terjual
        nasi_dine_in += 2*barang_terjual
        es_teh_dine_in += 2*barang_terjual
        terong_crispy += 2*barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual

    # Manis Berdua, ayam manis, ayam crispy, 2 nasi, 2 minum, 2 tahu, 4 chicken skin (DINE IN)
    elif sku == '10910690':
        ayam_geprek_crispy += 2*barang_terjual
        topping_manis += barang_terjual
        paper_cost_dine_in += 2*barang_terjual
        nasi_dine_in += 2*barang_terjual
        es_teh_dine_in += 2*barang_terjual
        tahu_crispy += 2*barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual

    # Special Berdua, ayam crisbar, ayam keju, 2 nasi, 2 minum, 2 tempe, 4 chicken skin
    elif sku == '10910190':
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += barang_terjual
        topping_keju += barang_terjual
        paper_cost_dine_in += 2*barang_terjual
        nasi_dine_in += 2*barang_terjual
        es_teh_dine_in += 2*barang_terjual
        dua_chicken_skin_crispy += 2*barang_terjual

    # paket crisbar, paket keju, 2 minum+ 2 tempe + 2 chicken skin
    elif sku == '10911590':
        ayam_geprek_crispy += 2*barang_terjual
        topping_crisbar += barang_terjual
        topping_keju += barang_terjual
        es_teh_dine_in += barang_terjual
        tempe_crispy += barang_terjual
        dua_chicken_skin_crispy += barang_terjual
        
    else:
        print(sku + ' - ' + nama_item + ' - ' + str(barang_terjual))

# 10200284 seharusnya orange

# BLOCK
print('ayam crispy : ' + str(ayam_crispy))
print('paper cost takeayaw l : ' + str(paper_cost_takeaway_l))
print('paper cost takeaway m : ' + str(paper_cost_takeaway_m))
print('paper cost takeaway paper bag : ' + str(paper_cost_takeaway_paper_bag))
print('packaging frozen : ' + str(packaging_frozen))
print('paper cost dine in : ' + str(paper_cost_dine_in))
print('ayam geprek crispy : ' + str(ayam_geprek_crispy))
print('upsize double chiken online : ' + str(upsize_double_chiken_online))
print('upsize double chiken dine in : ' + str(upsize_double_chiken_dine_in))
print('topping bbq cheese : ' + str(topping_bbq_cheese))
print('topping bbq gravy : ' + str(topping_bbq_gravy))
print('topping crisbar : ' + str(topping_crisbar))
print('topping matah : ' + str(topping_matah))
print('topping mamah : ' + str(topping_mamah))
print('topping tomat : ' + str(topping_tomat))
print('topping manis : ' + str(topping_manis))
print('topping goang : ' + str(topping_goang))
print('topping keju : ' + str(topping_keju))
print('topping crisbar madu : ' + str(topping_crisbar_madu))
print('topping crisbar frozen : ' + str(topping_crisbar_frozen))
print('topping mamah frozen : ' + str(topping_mamah_frozen))
print('kuah tongseng : ' + str(kuah_tongseng))
print('nasi dine in : ' + str(nasi_dine_in))
print('es teh dine in : ' + str(es_teh_dine_in))
print('lemon tea dine in : ' + str(lemon_tea_dine_in))
print('lemonade dine in : ' + str(lemonade_dine_in))
print('milo dine in : ' + str(milo_dine_in))
print('orange dine in : ' + str(orange_dine_in))
print('tahu crispy : ' + str(tahu_crispy))
print('tempe crispy : ' + str(tempe_crispy))
print('terong crispy : ' + str(terong_crispy))
print('telur sayur : ' + str(telur_sayur))
print('2 chicken skin crispy : ' + str(dua_chicken_skin_crispy))
print('nugget : ' + str(nugget))
print('kerupuk : ' + str(kerupuk))
print('kurma : ' + str(kurma))
print('puding milo dino : ' + str(puding_milo_dino))
print('lalab : ' + str(lalab))
print('nasi takeaway : ' + str(nasi_takeaway))
print('es teh takeaway : ' + str(es_teh_takeaway))
print('lemon tea takeaway : ' + str(lemon_tea_takeaway))
print('lemonade takeaway : ' + str(lemonade_takeaway))
print('milo takeaway : ' + str(milo_takeaway))
print('minum : ' + str(minum))
print('orange takeaway : ' + str(orange_takeaway))
print('sjora mango peach : ' + str(sjora_mango_peach))
print('kol crispy : ' + str(kol_crispy)) 

# PCS
ayam_SKH30010101 = (1*ayam_crispy) + (1*ayam_geprek_crispy) + (1*upsize_double_chiken_online) + (1*upsize_double_chiken_dine_in)

# liter
minyak_goreng_GNM10010201 = 0
minyak_goreng_GNM10010201 += (0.13*ayam_crispy)
minyak_goreng_GNM10010201 += (0.13*ayam_geprek_crispy)
minyak_goreng_GNM10010201 += (0.13*upsize_double_chiken_online)
minyak_goreng_GNM10010201 += (0.13*upsize_double_chiken_dine_in)
minyak_goreng_GNM10010201 += (0.0151515151515152*topping_matah)
minyak_goreng_GNM10010201 += (0.005*topping_goang)
minyak_goreng_GNM10010201 += (0.02*topping_crisbar_frozen)
minyak_goreng_GNM10010201 += (0.011111*topping_mamah_frozen)
minyak_goreng_GNM10010201 += (0.02*topping_mamah_frozen)
minyak_goreng_GNM10010201 += (0.02*tahu_crispy)
minyak_goreng_GNM10010201 += (0.02*tempe_crispy)
minyak_goreng_GNM10010201 += (0.02*terong_crispy)
minyak_goreng_GNM10010201 += (0.06*telur_sayur)
minyak_goreng_GNM10010201 += (0.02*dua_chicken_skin_crispy)
minyak_goreng_GNM10010201 += (0.02*kol_crispy)

# Gram
marinasi_MCN20040101 = (2.7*ayam_crispy) + (2.7*ayam_geprek_crispy) + (2.7*upsize_double_chiken_online)

# Gram
tepung_racik_RJC10020101 = 0
tepung_racik_RJC10020101 += (50*ayam_crispy)
tepung_racik_RJC10020101 += (6.667*ayam_crispy)
tepung_racik_RJC10020101 += (50*ayam_geprek_crispy)
tepung_racik_RJC10020101 += (7*ayam_geprek_crispy)
tepung_racik_RJC10020101 += (50*upsize_double_chiken_online)
tepung_racik_RJC10020101 += (7*upsize_double_chiken_online)
tepung_racik_RJC10020101 += (50*upsize_double_chiken_dine_in)
tepung_racik_RJC10020101 += (7*upsize_double_chiken_dine_in)
tepung_racik_RJC10020101 += (12.3456790*tahu_crispy)
tepung_racik_RJC10020101 += (12.3456790*tempe_crispy)
tepung_racik_RJC10020101 += (37.037*terong_crispy)
tepung_racik_RJC10020101 += (50*dua_chicken_skin_crispy)
tepung_racik_RJC10020101 += (7*dua_chicken_skin_crispy)
tepung_racik_RJC10020101 += (37.037*kol_crispy)

# ml
air_galon_AIR10010101 = 0
air_galon_AIR10010101 += (20*ayam_crispy)
air_galon_AIR10010101 += (20*ayam_geprek_crispy)
air_galon_AIR10010101 += (20*upsize_double_chiken_online)
air_galon_AIR10010101 += (20*upsize_double_chiken_dine_in)
air_galon_AIR10010101 += (20*topping_crisbar)
air_galon_AIR10010101 += (20*topping_crisbar_frozen)
air_galon_AIR10010101 += (172.5*nasi_dine_in)
air_galon_AIR10010101 += (375*es_teh_dine_in)
air_galon_AIR10010101 += (250*lemon_tea_dine_in)
air_galon_AIR10010101 += (250*lemonade_dine_in)
air_galon_AIR10010101 += (250*milo_dine_in)
air_galon_AIR10010101 += (250*orange_dine_in)
air_galon_AIR10010101 += (18.51852*tahu_crispy)
air_galon_AIR10010101 += (18.51852*tempe_crispy)
air_galon_AIR10010101 += (18.51852*terong_crispy)
air_galon_AIR10010101 += (20*dua_chicken_skin_crispy)
air_galon_AIR10010101 += (70*puding_milo_dino)
air_galon_AIR10010101 += (123.214*nasi_takeaway)
air_galon_AIR10010101 += (281.25*es_teh_takeaway)
air_galon_AIR10010101 += (250*lemon_tea_takeaway)
air_galon_AIR10010101 += (250*lemonade_takeaway)
air_galon_AIR10010101 += (250*milo_takeaway)
air_galon_AIR10010101 += (250*orange_takeaway)
air_galon_AIR10010101 += (18.51852*kol_crispy)

# PCS
box_packaging_takeaway_combo_BGP10010101 = (1*paper_cost_takeaway_l)

# Gram
selada_bokor_RJC20070101 = (13*paper_cost_takeaway_l) + (13*telur_sayur) + (10*paper_cost_takeaway_m)

# Pack
handglove_plastik_osaka_MLP10090201 = (0.01*paper_cost_takeaway_l) + (0.01*paper_cost_takeaway_m)

# Pack
tisu_livi_luncheon_100s_GNM10020201 = (0.01*paper_cost_takeaway_l) # paper cost dine in coklat bunga?

# Pack
kresek_24_putih_tristar_MLP10070201 = (0.01*paper_cost_takeaway_l) + (0.01*paper_cost_takeaway_m)

# Gram
bawang_putih_biasa_RJC10010101 = (3*ayam_geprek_crispy) + (3*upsize_double_chiken_online) + (3*upsize_double_chiken_dine_in) + (0.5*topping_crisbar_frozen) + (1.11*topping_mamah_frozen)

# Gram
maggie_lezat_NES10050201 = (3*ayam_geprek_crispy) + (3*upsize_double_chiken_online) + (3*upsize_double_chiken_dine_in) + (2*telur_sayur)

# Gram
kemangi_RJC20060101 = (4*ayam_geprek_crispy) + (4*upsize_double_chiken_online) + (4*upsize_double_chiken_dine_in)

# Gram
bumbu_crisbar_MCN20050101 = (8*topping_crisbar)

# Gram
bawang_bombay_RJC10180101 = (15.151515*topping_matah)

# Gram
sambal_matah_MCN20010101 = (13*topping_matah)

# Gram
sambal_mamah_MCN20030101 = (27*topping_mamah)

# Gram
sambal_tomat_MCN20020101 = (27*topping_tomat)

# Gram
gula_merah_TNM10020201 = (10*topping_manis) + (2.5*topping_crisbar_frozen) + (2.333*topping_mamah_frozen)

# Gram
tomat_kecil_RJC20110101 = (20*topping_goang)

# Gram
keju_wincheese_TNM10030201 = (20*topping_keju)

# Gram
bawang_merah_biasa_RJC10200101 = (0.5*topping_crisbar_frozen) + (2.778*topping_mamah_frozen)

# Gram
kecap_abc_TNM10080201 = (2.5*topping_crisbar_frozen) + (2.77778*topping_mamah_frozen)

# Gram
merica_TNM10120201 = (0.1*topping_crisbar_frozen)

# Gram
saus_tiram_lee_kum_kee_TNM10090201 = (0.6*topping_crisbar_frozen)

# Gram
dauh_salam_RJC20050101 = (0.1111*topping_mamah_frozen)

# Gram
ketumbar_TNM10110101 = (0.25*topping_crisbar_frozen)

# Gram
maizenna_maizenaku_TNM10100101 = (0.3*topping_crisbar_frozen)

# Pack
plastik_pe_7x15_tomat_MLP10150201 = (0.02*topping_crisbar_frozen) + (0.02*topping_mamah_frozen) + (1*kurma)

# Gram
cabe_merah_tw_RJC20220101 = (11.11*topping_mamah_frozen)

# Gram
cabe_keriting_biasa_RJC20210101 = (5.55556*topping_mamah_frozen)

# Gram
terasi_abc_TNM10160101 = (0.2222*topping_mamah_frozen)

# Gram
serah_RJC20250101 = (0.11111*topping_mamah_frozen)

# Gram
garam_kapal_TNM10050201 = (0.3333333*topping_mamah_frozen)

# Gram
msg_sasa_TNM10070201 = (0.22222*topping_mamah_frozen)

# Gram
gula_putih_indolampung_TNM10010101 = (0.888889*topping_mamah_frozen) + (20*puding_milo_dino)

# Gram
beras_putih_RJC10160201 = (150*nasi_dine_in) + (107.142*nasi_takeaway)

# Pack
kertas_nasi_putih_MLP10050201 = (0.01*nasi_takeaway)

# Bungkus
teh_manis_teh_sisri_FRS10010201 = (1.25*es_teh_dine_in) + (0.9375*es_teh_takeaway)

# Gram
es_batu_ATL30010201 = (100*es_teh_dine_in) + (100*lemon_tea_dine_in) + (100*lemonade_dine_in)
es_batu_ATL30010201 += (100*milo_dine_in)
es_batu_ATL30010201 += (100*orange_dine_in)
es_batu_ATL30010201 += (100*es_teh_takeaway)
es_batu_ATL30010201 += (100*lemon_tea_takeaway)
es_batu_ATL30010201 += (100*lemonade_takeaway)
es_batu_ATL30010201 += (100*milo_takeaway)
es_batu_ATL30010201 += (100*orange_takeaway)

# Gr
lemon_tea_NES10040201 = (31.25*lemon_tea_dine_in) + (31.25*lemon_tea_takeaway)

# Gr
lemonade_NES10030201 = (20*lemonade_dine_in) + (20*lemonade_takeaway)

# Gr
milo_NES10020201 = (30*milo_dine_in) + (10*puding_milo_dino) + (30*milo_takeaway)

# Gr
orange_NES10010201 = (17.5*orange_dine_in) + (17.5*orange_takeaway)

# Pcs
tahu_RJC20080101 = (1*tahu_crispy)

# Gram
terong_ungu_biasa_RJC20100101 = (83.333*terong_crispy)

# Pcs
telur_TNH10020201 = (1*telur_sayur)

# Gram
kulit_ayam_TNH30010101 = (40*dua_chicken_skin_crispy)

# Pcs
kerupuk_RJC10150101 = (1*kerupuk)

# Pcs
pudding_nutrijel_cokelat_FRS10020201 = (0.0083333*puding_milo_dino)

# Pcs
sendok_puding_727_MLP10140201 = (1*puding_milo_dino)

# Pcs
cup_puding_MLP10130101 = (1*puding_milo_dino)

# Pcs
gelas_cup_plastik_120z_MLP10010101 = (1*es_teh_takeaway) + (1*lemon_tea_takeaway) + (1*lemonade_takeaway) + (1*milo_takeaway) + (1*orange_takeaway)

# Rol
seal_cup_plastik_MLP10020101 = (0.000909090909090909*es_teh_takeaway) + (0.000909090909090909*lemon_tea_takeaway) + (0.000909090909090909*lemonade_takeaway) + (0.000909090909090909*milo_takeaway) + (0.000909090909090909*orange_takeaway)

# Pack
keresek_15_putih_tristar_MLP10060201 = (0.01*es_teh_takeaway) + (0.01*lemon_tea_takeaway) + (0.01*lemonade_takeaway) + (0.01*milo_takeaway) + (0.01*orange_takeaway)

# Gram
kol_RJC20030101 = (50*kol_crispy)

# Pcs
box_packaging_alacarte_BGP10020101 = (1*paper_cost_takeaway_m)

# Pcs
box_packaging_paper_bag_BGP10040101 = (1*paper_cost_takeaway_paper_bag)

# Papan
tempe_RJC20090101 = (0.0625)*tempe_crispy

# ------------------------------------------------------------ EDIT YANG DI BAWAH AJA ----------------------------------------------------------------

isi = ''
isi += 'SKU;Nama Item;Satuan;Sold\n'
isi += 'MCN20030101;Sambal Mamah;Gram;' + str(sambal_mamah_MCN20030101).replace('.',',') + '\n'
isi += 'MCN20020101;Sambal Tomat;Gram;' + str(sambal_tomat_MCN20020101).replace('.',',') + '\n'
isi += 'MCN20010101;Sambal Matah;Gram;' + str(sambal_matah_MCN20010101).replace('.',',') + '\n'
isi += 'MCN20050101;Bumbu Crisbar;Gram;' + str(bumbu_crisbar_MCN20050101).replace('.',',') + '\n'
isi += 'MCN20060101;JRBCSS 523 G;Gram;' + str(0) + '\n'

isi += 'SKH30010101;Ayam;Pcs;' + str(ayam_SKH30010101).replace('.',',') + '\n'
isi += 'BGP10010101;Box Packaging Take Away Combo;Pcs;' + str(box_packaging_takeaway_combo_BGP10010101).replace('.',',') + '\n'
isi += 'BGP10020101;Box Packaging Alacarte;Pcs;' + str(box_packaging_alacarte_BGP10020101).replace('.',',') + '\n'
isi += 'BGP10040101;Box Packaging Paper Bag;Pcs;' + str(box_packaging_paper_bag_BGP10040101).replace('.',',') + '\n'
isi += 'SPD10020101;Paperbowl 5 oz;Pcs;' + '0\n'

isi += 'RJC10160201;Beras Putih;Gram;' + str(beras_putih_RJC10160201).replace('.',',') + '\n'
isi += 'RJC10020101;Tepung Racik;Gram;' + str(tepung_racik_RJC10020101).replace('.',',') + '\n'

isi += 'RJC10010101;Bawang Putih Kupas;Gram;' + str(bawang_putih_biasa_RJC10010101).replace('.',',') + '\n'
isi += 'RJC20040101;Cengek Domba Lembang;Gram;' + '0\n'
isi += 'RJC20080101;Tahu;Pcs;' + str(tahu_RJC20080101).replace('.',',') + '\n'
isi += 'RJC20090101;Tempe;Papan;' + str(tempe_RJC20090101).replace('.',',') + '\n'
isi += 'RJC20070101;Selada Bokor;Gram;' + str(selada_bokor_RJC20070101).replace('.',',') + '\n'
isi += 'RJC20060101;Kemangi;Gram;' + str(kemangi_RJC20060101).replace('.',',') + '\n'
isi += 'RJC20030101;Kol;Gram;' + str(kol_RJC20030101).replace('.',',') + '\n'
isi += 'RJC20050101;Daun Salam;Gram;' + str(dauh_salam_RJC20050101).replace('.',',') + '\n'
isi += 'RJC20100101;Terong Ungu Biasa;Gram;' + str(terong_ungu_biasa_RJC20100101).replace('.',',') + '\n'
isi += 'RJC20110101;Tomat Kecil;Gram;' + str(tomat_kecil_RJC20110101).replace('.',',') + '\n'
isi += 'RJC10150101;Kerupuk;Pcs;' + str(kerupuk_RJC10150101).replace('.',',') + '\n'
isi += 'ATL30010201;Es Batu;Gram;' + str(es_batu_ATL30010201).replace('.',',') + '\n'
isi += 'AIR10010101;Air Galon;ml;' + str(air_galon_AIR10010101).replace('.',',') + '\n'

isi += 'TNM10030201;Minyak Goreng;L;' + str(minyak_goreng_GNM10010201).replace('.',',') + '\n'
isi += 'RJC10180101;Bawang Bombay;Gram;' + str(bawang_bombay_RJC10180101).replace('.',',') + '\n'
isi += 'RJC10190101;Saos Sambal Sachet SASA;Sachet;' + str(0) + '\n'
isi += 'TNH30010101;Kulit Ayam;Gram;' + str(kulit_ayam_TNH30010101).replace('.',',') + '\n'
isi += 'TNH10020201;Telur;Pcs;' + str(telur_TNH10020201).replace('.',',') + '\n'
isi += 'TNM10020201;Gula Merah;Gram;' + str(gula_merah_TNM10020201).replace('.',',') + '\n'
isi += 'TNM10030201;Keju (Wincheese);Gram;' + str(keju_wincheese_TNM10030201).replace('.',',') + '\n'
isi += 'TNM10080201;Kecap (ABC);Gram;' + str(kecap_abc_TNM10080201).replace('.',',') + '\n'
isi += 'FRS10030201;Silky Pudding Biscuit;Pcs;' + str(0) + '\n'
isi += 'FRS10010201;Teh Manis (Teh Sisri);Bungkus;' + str(teh_manis_teh_sisri_FRS10010201).replace('.',',') + '\n'
isi += 'NES10010201;Orange;Gr;' + str(orange_NES10010201).replace('.',',') + '\n'
isi += 'NES10020201;Milo;Gr;' + str(milo_NES10020201).replace('.',',') + '\n'
isi += 'NES10040201;Lemon Tea;Gr;' + str(lemon_tea_NES10040201).replace('.',',') + '\n'
isi += 'NES10050201;Maggie Lezat;Gram;' + str(maggie_lezat_NES10050201).replace('.',',') + '\n'

isi += "GNM10020201;Tisu (Livi Multipurpose Eco 200's);Pack;" + str(tisu_livi_luncheon_100s_GNM10020201).replace('.',',') + '\n'
isi += 'GNM10030201;Tisu (Livi Kitchen Towel);Roll;' + str(0) + '\n'
isi += "GNM10040201;Lakban bening 1/2';Pcs;" + str(0) + '\n'
isi += 'MLP10010101;Gelas Cup Plastik 12 oz;Pcs;' + str(gelas_cup_plastik_120z_MLP10010101).replace('.',',') + '\n'
isi += 'MLP10020101;Seal Cup Plastik;Rol;' + str(seal_cup_plastik_MLP10020101).replace('.',',') + '\n'
isi += 'MLP10040201;Kertas Nasi Bunga 25 (Gajah);Pack;' + str(0) + '\n'
isi += 'MLP10050201;Kertas Nasi Putih;Pack;' + str(kertas_nasi_putih_MLP10050201).replace('.',',') + '\n'
isi += 'MLP10060201;Kresek 15 Putih (Tristar);Pack;' + str(keresek_15_putih_tristar_MLP10060201).replace('.',',') + '\n'
isi += 'MLP10070201;Kresek 24 Putih (Tristar);Pack;' + str(kresek_24_putih_tristar_MLP10070201).replace('.',',') + '\n'
isi += 'MLP10190201;Kresek 40 Putih (Tulip);Pack;' + str(0) + '\n'
isi += 'MLP10080201;Trashbag 80 x 120 (Tulip);Pack;' + str(0) + '\n'
isi += 'MLP10090201;Handglove Plastik (Osaka);Pack;' + str(handglove_plastik_osaka_MLP10090201).replace('.',',') + '\n'
isi += 'MLP10100101;Karet;Bungkus;' + str(0) + '\n'
isi += 'MLP10120201;Zip Plastik 7x10;Pack;' + str(0) + '\n'
isi += 'MLP10180101;Plastik PE 15x30 (Uk 1Kg);Pack;' + str(0) + '\n'
isi += 'MLP10160201;Plastik PE (Uk 2Kg);Pack;' + str(0) + '\n'
isi += 'MLP10130101;Cup Pudding 200 ML;Pcs;' + str(cup_puding_MLP10130101).replace('.',',') + '\n'
isi += 'MLP10140201;Sendok Pudding (727);Pcs;' + str(sendok_puding_727_MLP10140201).replace('.',',') + '\n'
isi += 'MLP10200101;Ripet ikat;Pack;' + str(0) + '\n'
isi += 'TNM10100201;Packaging Polos;Pcs;' + str(0) + '\n'
isi += 'XYZ10010201;Pembersih lantai floor;ML;' + str(0) + '\n'
isi += 'XYZ10020201;Handsoap;ML;' + str(0) + '\n'
isi += 'XYZ10030201;Karbol;ML;' + str(0) + '\n'
isi += 'XYZ10040101;Anti Lalat;ML;' + str(0) + '\n'
isi += 'XYZ10050201;Multy Purpose (Sabun Cuci);ML;' + str(0) + '\n'
isi += 'XYZ10060201;Laundry Liquid detergen;ML;' + str(0) + '\n'

# isi += 'MCN2004010;Marinasi;Gram;' + str(marinasi_MCN20040101).replace('.',',') + '\n'
# isi += 'NES10030201;Lemonade;Gr;' + str(lemonade_NES10030201).replace('.',',') + '\n'
# isi += 'RJC10200101;Bawang Merah Biasa;Gram;' + str(bawang_merah_biasa_RJC10200101).replace('.',',') + '\n'
# isi += 'TNM10120201;Merica (Saerah);Gram;' + str(merica_TNM10120201).replace('.',',') + '\n'
# isi += 'TNM10090201;Saus Tiram (Lee Kum Kee);Gram;' + str(saus_tiram_lee_kum_kee_TNM10090201).replace('.',',') + '\n'
# isi += 'TNM10110101;Ketumbar;Gram;' + str().replace('.',',') + '\n'
# isi += 'TNM10100101;Maizenna (Maizenaku);Gram;' + str(maizenna_maizenaku_TNM10100101).replace('.',',') + '\n'
# isi += 'MLP10150201;Plastik PE 7x15 (Tomat);Pack;' + str(plastik_pe_7x15_tomat_MLP10150201).replace('.',',') + '\n'
# isi += 'RJC20220101;Cabe Merah TW;Gram;' + str(cabe_merah_tw_RJC20220101).replace('.',',') + '\n'
# isi += 'RJC20210101;Cabe Keriting Biasa;Gram;' + str(cabe_keriting_biasa_RJC20210101).replace('.',',') + '\n'
# isi += 'TNM10160101;Terasi (ABC);Gram;' + str(terasi_abc_TNM10160101).replace('.',',') + '\n'
# isi += 'RJC20250101;Sereh;Gram;' + str(serah_RJC20250101).replace('.',',') + '\n'
# isi += 'TNM10050201;Garam (Kapal);Gram;' + str(garam_kapal_TNM10050201).replace('.',',') + '\n'
# isi += 'TNM10070201;MSG (Sasa);Gram;' + str(msg_sasa_TNM10070201).replace('.',',') + '\n'
# isi += 'TNM10010101;Gula Putih (Indolampung);Gram;' + str(gula_putih_indolampung_TNM10010101).replace('.',',') + '\n'
# isi += 'FRS10020201;Pudding (Nutrijel) Cokelat;Pcs;' + str(pudding_nutrijel_cokelat_FRS10020201).replace('.',',') + '\n'


print(isi)

hasil = open('Data Sold - ' + cabang + '.csv','w')
hasil.write(isi)
hasil.close()