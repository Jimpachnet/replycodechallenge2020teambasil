def calculate_potential(w1, w2):
    wp = 0
    if type(w1) == "Developer" and type(w2) == "Developer":
        skill_union = len(w1.skillset | w2.skillset)
        skill_xor = len(w1.skillset - w1.skillset)
        wp = skill_union * skill_xor

    bp = 0
    if w1.company == w2.company:
        bp = w1.bonus * w1.bonus

    return wp+bp
