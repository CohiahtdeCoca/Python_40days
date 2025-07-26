def calculate_can_chi_calendar(year):
    can_list=['Giáp', 'Ất', 'Bính', 'Đinh', 'Mậu', 'Kỷ', 'Canh', 'Tân', 'Nhâm', 'Quý']
    chi_list=['Tý', 'Sửu', 'Dần', 'Mão', 'Thìn', 'Tỵ', 'Ngọ', 'Mùi', 'Thân', 'Dậu', 'Tuất', 'Hợi']
    year_adjust = year - 4
    can = can_list[year_adjust % 10]
    chi = chi_list[year_adjust % 12]
    return f"Năm {year} là năm {can} {chi}"

year_input = int(input("Nhập năm dương lịch: "))
print(calculate_can_chi_calendar(year_input))
