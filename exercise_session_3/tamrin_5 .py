def bernoulli_numbers(tedad):
    bernoulli_list = [1] 
    for m in range(1, tedad + 1):
        bernoulli_list.append(0)
        for j in range(m, 0, -1):
            bernoulli_list[j - 1] = j * (bernoulli_list[j - 1] - bernoulli_list[j])
    return bernoulli_list
tedad = int(input("Tedad_adad_donbale_Bernoulli_ra_vared_konid:) "))
bernoulli_sequence = bernoulli_numbers(tedad)
print("Donbale_Bernoulli_ta_adad", tedad, "ebarat_ast_az:")
print(bernoulli_sequence)