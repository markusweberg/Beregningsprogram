import _tkinter
import tkinter as tk
import tkinter.messagebox
import pandas as pd
import numpy as np
from rapport_pdf import create_pdf


def velkomst():
    tk.messagebox.showinfo('Velkommen', 'Regler for utfylling av gulv-egenskaper:\n\nEnten:\n'
                                        'Fyll ut gulvklasse OG ønsket armeringstype/størrelse'
                                        '\nEller:\nFyll ut alle felt utenom gulvklasse for egendefinerte'
                                        ' krav\n\nTips: Velg "Ingen krav" så vil alle valgene i menyen '
                                        'velges!', master=window)


def loads(truck_pick, truck_dict, dekk_pick, dekk_dict, bil_pick, bil_dict, nytte_pick, nytte_dict, egendef_last, rd):
    global q_ed
    try:
        if len(dekk_pick.get()) != 0 and len(truck_pick.get()) != 0 and truck_dict[truck_pick.get()] != 0:
            dekk_faktor = float(dekk_dict[dekk_pick.get()])
            truck_q = float(truck_dict[truck_pick.get()])
            q_ed = truck_q * (dekk_faktor * 1000 / 2)
            df['r'] = (200 / np.pi**(1 / 2))
        elif len(bil_pick.get()) != 0 and bil_dict[bil_pick.get()] != 0:
            bil_last = float(bil_dict[bil_pick.get()])
            q_ed = bil_last * 1000 / 2
            if bil_pick.get() == 'Kategori F':
                df['r'] = (100 / np.pi**(1 / 2))
            if bil_pick.get() == 'Kategori G':
                df['r'] = (200 / np.pi**(1 / 2))
        elif len(nytte_pick.get()) != 0 and nytte_dict[nytte_pick.get()] != 0:
            nytte_last = float(nytte_dict[nytte_pick.get()])
            q_ed = nytte_last * 1000
            df['r'] = (50 / np.pi**(1 / 2))
        else:
            q_ed = float(egendef_last.get()) * 1000
            df['r'] = float(rd.get())
        print(q_ed)
    except ValueError:
        tk.messagebox.showinfo('Feilmelding', '- Fyll inn alle felt \n- Bruk punktum som desimalskille'
                                              '\n- Utfyllbare felt skal bare inneholde tall', master=window)


def loads_2(truck_pick, truck_dict, dekk_pick, dekk_dict, bil_pick, bil_dict, nytte_pick, nytte_dict, egendef_last, rd):
    global q_ed
    try:
        if len(dekk_pick.get()) != 0 and len(truck_pick.get()) != 0 and truck_dict[truck_pick.get()] != 0:
            dekk_faktor = float(dekk_dict[dekk_pick.get()])
            truck_q = float(truck_dict[truck_pick.get()])
            q_ed = truck_q * (dekk_faktor * 1000 / 2)
            df_2['r'] = (200 / np.pi**(1 / 2))
        elif len(bil_pick.get()) != 0 and bil_dict[bil_pick.get()] != 0:
            bil_last = float(bil_dict[bil_pick.get()])
            q_ed = bil_last * 1000 / 2
            if bil_pick.get() == 'Kategori F':
                df_2['r'] = (100 / np.pi**(1 / 2))
            if bil_pick.get() == 'Kategori G':
                df_2['r'] = (200 / np.pi**(1 / 2))
        elif len(nytte_pick.get()) != 0 and nytte_dict[nytte_pick.get()] != 0:
            nytte_last = float(nytte_dict[nytte_pick.get()])
            q_ed = nytte_last * 1000
            df_2['r'] = (50 / np.pi**(1 / 2))
        else:
            q_ed = float(egendef_last.get()) * 1000
            df_2['r'] = float(rd.get())
    except:
        pass


def loads_3(truck_pick, truck_dict, dekk_pick, dekk_dict, bil_pick, bil_dict, nytte_pick, nytte_dict, egendef_last, rd):
    global q_ed
    try:
        if len(dekk_pick.get()) != 0 and len(truck_pick.get()) != 0 and truck_dict[truck_pick.get()] != 0:
            dekk_faktor = float(dekk_dict[dekk_pick.get()])
            truck_q = float(truck_dict[truck_pick.get()])
            q_ed = truck_q * (dekk_faktor * 1000 / 2)
            df_3['r'] = (200 / np.pi**(1 / 2))
        elif len(bil_pick.get()) != 0 and bil_dict[bil_pick.get()] != 0:
            bil_last = float(bil_dict[bil_pick.get()])
            q_ed = bil_last * 1000 / 2
            if bil_pick.get() == 'Kategori F':
                df_3['r'] = (100 / np.pi**(1 / 2))
            if bil_pick.get() == 'Kategori G':
                df_3['r'] = (200 / np.pi**(1 / 2))
        elif len(nytte_pick.get()) != 0 and nytte_dict[nytte_pick.get()] != 0:
            nytte_last = float(nytte_dict[nytte_pick.get()])
            q_ed = nytte_last * 1000
            df_3['r'] = (50 / np.pi**(1 / 2))
        else:
            q_ed = float(egendef_last.get()) * 1000
            df_3['r'] = float(rd.get())
    except:
        pass


def input_calc(concrete_price_m40, concrete_price_m45, concrete_price_m60, concrete_gwp_m40,
               concrete_gwp_m45, concrete_gwp_m60, rebar_price, rebar_gwp, red_factor, stiffness,
               x, y, c_nom, k_dict, k_pick, iso_dict, iso_pick, iso_thickness):
    global check
    try:
        # User input
        df.loc[df['concrete_quality'] == 'B45 M40', 'concrete_price_input'] = float(concrete_price_m40.get())
        df.loc[df['concrete_quality'] == 'B35 M45', 'concrete_price_input'] = float(concrete_price_m45.get())
        df.loc[df['concrete_quality'] == 'B30 M60', 'concrete_price_input'] = float(concrete_price_m60.get())
        df['rebar_price_input'] = float(rebar_price.get())
        df.loc[df['concrete_quality'] == 'B45 M40', 'concrete_gwp_input'] = float(concrete_gwp_m40.get())
        df.loc[df['concrete_quality'] == 'B35 M45', 'concrete_gwp_input'] = float(concrete_gwp_m45.get())
        df.loc[df['concrete_quality'] == 'B30 M60', 'concrete_gwp_input'] = float(concrete_gwp_m60.get())
        df['rebar_gwp_input'] = float(rebar_gwp.get())
        df['reduction_factor_sigma_s2'] = float(red_factor.get())
        df['x'] = float(x.get())
        df['y'] = float(y.get())
        df['c_nom'] = float(c_nom.get())
        if len(k_pick.get()) == 0 or float(k_dict[k_pick.get()]) == 0:
            df['k'] = float(stiffness.get())
            if len(iso_pick.get()) == 0 or float(iso_dict[iso_pick.get()]) == 0 or float(iso_thickness.get()) == 0:
                df['k'] = float(stiffness.get())
            else:
                df['k'] = float(iso_dict[iso_pick.get()]) / float(iso_thickness.get())
        else:
            df['k'] = float(k_dict[k_pick.get()])
        # Calculations, filling the csv file with data
        df['rebar_price'] = df['rebar_price_input'] * df['rebar_per_square_meter_sum']
        df['concrete_price'] = df['concrete_price_input'] * df['concrete_per_square_meter']
        df['price_sum'] = df['rebar_price'] + df['concrete_price']
        df['concrete_gwp'] = df['concrete_gwp_input'] * df['concrete_per_square_meter']
        df['rebar_gwp'] = df['rebar_gwp_input'] * df['rebar_per_square_meter_sum']
        df['gwp_sum'] = df['concrete_gwp'] + df['rebar_gwp']
        df.loc[df['r'] < df['r_limit'], 'a'] = (1.6*df['r']**2+df['thickness']**2)**(1 / 2) - (0.675*df['thickness'])
        df.loc[df['r'] >= df['r_limit'], 'a'] = df['r']
        df.loc[df['reduction_factor_sigma_s2'] != 1, 'w_2'] = df['w'] * (df['reduction_factor_sigma_s2'])**2
        df.loc[df['reduction_factor_sigma_s2'] == 1, 'w_2'] = df['w']
        df['l_e'] = (df['capital_d'] / df['k'])**(1 / 4)
        df['westergaard_center'] = df['f_ck'] * df['thickness']**2 / (1.32 * np.log10(1.43 * df['l_e'] / df['a']))
        df['westergaard_edge'] = df['f_ck'] * df['thickness']**2 / (2.34 * np.log10(1.23 * df['l_e'] / df['a']))
        df['westergaard_corner'] = df['f_ck'] * df['thickness']**2 / (3 * (1 - (1.23 * (df['a'] / df['l_e'])**0.6)))
        df.loc[df['rebar_size_lower'] == 0, 'd_eff'] = df['c_nom'] + df['rebar_size_upper']
        df.loc[df['rebar_size_lower'] != 0, 'd_eff'] = df['thickness'] - df['c_nom'] - df['rebar_size_lower']
        df['ro_l'] = df['a_s_total'] / (df['d_eff'] * 1000)
        df['k_ec2'] = 1 + (200 / df['d_eff'])**(1 / 2)
        df.loc[df['k_ec2'] > 2, 'k_ec2'] = 2
        df['u_1_center'] = 2 * np.pi * (df['r'] + 2 * df['d_eff'])
        df['u_1_edge'] = np.pi * (df['r'] + 2 * df['d_eff'])
        df['u_1_corner'] = np.pi * (df['r'] + 2 * df['d_eff']) / 2
        df['c_rdc'] = 0.1
        df['v_rd'] = df['c_rdc'] * df['k_ec2'] * (100 * df['ro_l'] * df['f_ck'])**(1 / 3)
        df['v_min'] = 0.035 * df['k_ec2']**(3 / 2) * df['f_ck']**(1 / 2)
        df.loc[df['v_rd'] > df['v_min'], 'v_rd_2'] = df['v_rd']
        df.loc[df['v_rd'] <= df['v_min'], 'v_rd_2'] = df['v_min']
        df['v_ed_1_center'] = df['v_rd_2'] * df['u_1_center'] *df['d_eff']
        df['v_ed_1_edge'] = df['v_rd_2'] * df['u_1_edge'] *df['d_eff']
        df['v_ed_1_corner'] = df['v_rd_2'] * df['u_1_corner'] *df['d_eff']
        df['u_0_center'] = 2 * np.pi * df['r']
        df['u_0_edge'] = np.pi * df['r']
        df['u_0_corner'] = np.pi * df['r'] / 2
        df['v_ed_0_center'] = df['v_rd_max'] * df['u_0_center'] * df['d_eff']
        df['v_ed_0_edge'] = df['v_rd_max'] * df['u_0_edge'] * df['d_eff']
        df['v_ed_0_corner'] = df['v_rd_max'] * df['u_0_corner'] * df['d_eff']
        df['meyerhof_center'] = 6 * (1 + 2 * df['a'] / df['l_e']) * (df['m_p'] / 10**3 + df['m_n'] / 10**3)
        df['meyerhof_edge'] = 3.5 * (1 + 3 * df['a'] / df['l_e']) * (df['m_p'] / 10**3 + df['m_n'] / 10**3)
        df['meyerhof_corner'] = 2 * (1 + 4 * df['a'] / df['l_e']) * df['m_n'] / 10**3
        df['a_l_e_limit'] = df['a'] / df['l_e']
        df.loc[df['a_l_e_limit'] < 0.2, 'dual_point_load'] = (2 * np.pi + 1.8 * df['x'] / df['l_e']) * \
                                                             (df['m_p'] / 10**3 + df['m_n'] / 10**3)
        df.loc[df['a_l_e_limit'] >= 0.2, 'dual_point_load'] = ((4 * np.pi / (1 - df['a'] / 3 * df['l_e'])) +
                                                              (1.8 * df['x'] / (df['l_e'] - df['a'] / 2))) * \
                                                              (df['m_p'] / 10**3 + df['m_n'] / 10**3)
        df.loc[df['a_l_e_limit'] < 0.2, 'quadruple_point_load'] = (2 * np.pi + 1.8 * (df['x'] + df['y']) /
                                                                   df['l_e']) * (df['m_p'] / 10**3 + df['m_n'] / 10**3)
        df.loc[df['a_l_e_limit'] >= 0.2, 'quadruple_point_load'] = ((4 * np.pi / (1 - df['a'] / 3 * df['l_e'])) +
                                                                    (1.8 * (df['x'] + df['y']) /
                                                                     (df['l_e'] - df['a'] / 2))) * \
                                                                      (df['m_p'] / 10**3 + df['m_n'] / 10**3)
    except _tkinter.TclError:
        tk.messagebox.showinfo('Feilmelding', '- Fyll inn alle felt \n- Bruk punktum som desimalskille'
                                              '\n- Utfyllbare felt skal bare inneholde tall', master=window)
    except ValueError:
        tk.messagebox.showinfo('Feilmelding', '- Fyll inn alle felt \n- Bruk punktum som desimalskille'
                                              '\n- Utfyllbare felt skal bare inneholde tall',
                               master=window)
    if (df['k'] == 0).all():
        tk.messagebox.showinfo('Feilmelding', 'Vennligst velg grunnforhold eller fyll ut grunnstivhet', master=window)
    else:
        check = 'Kalkulasjoner er gjort'


def input_calc_2(concrete_price_m40, concrete_price_m45, concrete_price_m60, concrete_gwp_m40,
               concrete_gwp_m45, concrete_gwp_m60, rebar_price, rebar_gwp, red_factor, stiffness,
               x, y, c_nom, k_dict, k_pick, iso_dict, iso_pick, iso_thickness):
    try:
        # User input
        df_2.loc[df_2['concrete_quality'] == 'B45 M40', 'concrete_price_input'] = float(concrete_price_m40.get())
        df_2.loc[df_2['concrete_quality'] == 'B35 M45', 'concrete_price_input'] = float(concrete_price_m45.get())
        df_2.loc[df_2['concrete_quality'] == 'B30 M60', 'concrete_price_input'] = float(concrete_price_m60.get())
        df_2['rebar_price_input'] = float(rebar_price.get())
        df_2.loc[df_2['concrete_quality'] == 'B45 M40', 'concrete_gwp_input'] = float(concrete_gwp_m40.get())
        df_2.loc[df_2['concrete_quality'] == 'B35 M45', 'concrete_gwp_input'] = float(concrete_gwp_m45.get())
        df_2.loc[df_2['concrete_quality'] == 'B30 M60', 'concrete_gwp_input'] = float(concrete_gwp_m60.get())
        df_2['rebar_gwp_input'] = float(rebar_gwp.get())
        df_2['reduction_factor_sigma_s2'] = float(red_factor.get())
        df_2['x'] = float(x.get())
        df_2['y'] = float(y.get())
        df_2['c_nom'] = float(c_nom.get())
        if len(k_pick.get()) == 0 or float(k_dict[k_pick.get()]) == 0:
            df_2['k'] = float(stiffness.get())
            if len(iso_pick.get()) == 0 or float(iso_dict[iso_pick.get()]) == 0 or float(iso_thickness.get()) == 0:
                df_2['k'] = float(stiffness.get())
            else:
                df_2['k'] = float(iso_dict[iso_pick.get()]) / float(iso_thickness.get())
        else:
            df_2['k'] = float(k_dict[k_pick.get()])
        # Calculations, filling the csv file with data
        df_2['rebar_price'] = df_2['rebar_price_input'] * df_2['rebar_per_square_meter_sum']
        df_2['concrete_price'] = df_2['concrete_price_input'] * df_2['concrete_per_square_meter']
        df_2['price_sum'] = df_2['rebar_price'] + df_2['concrete_price']
        df_2['concrete_gwp'] = df_2['concrete_gwp_input'] * df_2['concrete_per_square_meter']
        df_2['rebar_gwp'] = df_2['rebar_gwp_input'] * df_2['rebar_per_square_meter_sum']
        df_2['gwp_sum'] = df_2['concrete_gwp'] + df_2['rebar_gwp']
        df_2.loc[df_2['r'] < df_2['r_limit'], 'a'] = (1.6*df_2['r']**2+df_2['thickness']**2)**(1 / 2) - (0.675*df_2['thickness'])
        df_2.loc[df_2['r'] >= df_2['r_limit'], 'a'] = df_2['r']
        df_2.loc[df_2['reduction_factor_sigma_s2'] != 1, 'w_2'] = df_2['w'] * (df_2['reduction_factor_sigma_s2'])**2
        df_2.loc[df_2['reduction_factor_sigma_s2'] == 1, 'w_2'] = df_2['w']
        df_2['l_e'] = (df_2['capital_d'] / df_2['k'])**(1 / 4)
        df_2['westergaard_center'] = df_2['f_ck'] * df_2['thickness']**2 / (1.32 * np.log10(1.43 * df_2['l_e'] / df_2['a']))
        df_2['westergaard_edge'] = df_2['f_ck'] * df_2['thickness']**2 / (2.34 * np.log10(1.23 * df_2['l_e'] / df_2['a']))
        df_2['westergaard_corner'] = df_2['f_ck'] * df_2['thickness']**2 / (3 * (1 - (1.23 * (df_2['a'] / df_2['l_e'])**0.6)))
        df_2.loc[df_2['rebar_size_lower'] == 0, 'd_eff'] = df_2['c_nom'] + df_2['rebar_size_upper']
        df_2.loc[df_2['rebar_size_lower'] != 0, 'd_eff'] = df_2['thickness'] - df_2['c_nom'] - df_2['rebar_size_lower']
        df_2['ro_l'] = df_2['a_s_total'] / (df_2['d_eff'] * 1000)
        df_2['k_ec2'] = 1 + (200 / df_2['d_eff'])**(1 / 2)
        df_2.loc[df_2['k_ec2'] > 2, 'k_ec2'] = 2
        df_2['u_1_center'] = 2 * np.pi * (df_2['r'] + 2 * df_2['d_eff'])
        df_2['u_1_edge'] = np.pi * (df_2['r'] + 2 * df_2['d_eff'])
        df_2['u_1_corner'] = np.pi * (df_2['r'] + 2 * df_2['d_eff']) / 2
        df_2['c_rdc'] = 0.1
        df_2['v_rd'] = df_2['c_rdc'] * df_2['k_ec2'] * (100 * df_2['ro_l'] * df_2['f_ck'])**(1 / 3)
        df_2['v_min'] = 0.035 * df_2['k_ec2']**(3 / 2) * df_2['f_ck']**(1 / 2)
        df_2.loc[df_2['v_rd'] > df_2['v_min'], 'v_rd_2'] = df_2['v_rd']
        df_2.loc[df_2['v_rd'] <= df_2['v_min'], 'v_rd_2'] = df_2['v_min']
        df_2['v_ed_1_center'] = df_2['v_rd_2'] * df_2['u_1_center'] *df_2['d_eff']
        df_2['v_ed_1_edge'] = df_2['v_rd_2'] * df_2['u_1_edge'] *df_2['d_eff']
        df_2['v_ed_1_corner'] = df_2['v_rd_2'] * df_2['u_1_corner'] *df_2['d_eff']
        df_2['u_0_center'] = 2 * np.pi * df_2['r']
        df_2['u_0_edge'] = np.pi * df_2['r']
        df_2['u_0_corner'] = np.pi * df_2['r'] / 2
        df_2['v_ed_0_center'] = df_2['v_rd_max'] * df_2['u_0_center'] * df_2['d_eff']
        df_2['v_ed_0_edge'] = df_2['v_rd_max'] * df_2['u_0_edge'] * df_2['d_eff']
        df_2['v_ed_0_corner'] = df_2['v_rd_max'] * df_2['u_0_corner'] * df_2['d_eff']
        df_2['meyerhof_center'] = 6 * (1 + 2 * df_2['a'] / df_2['l_e']) * (df_2['m_p'] / 10**3 + df_2['m_n'] / 10**3)
        df_2['meyerhof_edge'] = 3.5 * (1 + 3 * df_2['a'] / df_2['l_e']) * (df_2['m_p'] / 10**3 + df_2['m_n'] / 10**3)
        df_2['meyerhof_corner'] = 2 * (1 + 4 * df_2['a'] / df_2['l_e']) * df_2['m_n'] / 10**3
        df_2['a_l_e_limit'] = df_2['a'] / df_2['l_e']
        df_2.loc[df_2['a_l_e_limit'] < 0.2, 'dual_point_load'] = (2 * np.pi + 1.8 * df_2['x'] / df_2['l_e']) * \
                                                             (df_2['m_p'] / 10**3 + df_2['m_n'] / 10**3)
        df_2.loc[df_2['a_l_e_limit'] >= 0.2, 'dual_point_load'] = ((4 * np.pi / (1 - df_2['a'] / 3 * df_2['l_e'])) +
                                                              (1.8 * df_2['x'] / (df_2['l_e'] - df_2['a'] / 2))) * \
                                                              (df_2['m_p'] / 10**3 + df_2['m_n'] / 10**3)
        df_2.loc[df_2['a_l_e_limit'] < 0.2, 'quadruple_point_load'] = (2 * np.pi + 1.8 * (df_2['x'] + df_2['y']) /
                                                                   df_2['l_e']) * (df_2['m_p'] / 10**3 + df_2['m_n'] / 10**3)
        df_2.loc[df_2['a_l_e_limit'] >= 0.2, 'quadruple_point_load'] = ((4 * np.pi / (1 - df_2['a'] / 3 * df_2['l_e'])) +
                                                                    (1.8 * (df_2['x'] + df_2['y']) /
                                                                     (df_2['l_e'] - df_2['a'] / 2))) * \
                                                                      (df_2['m_p'] / 10**3 + df_2['m_n'] / 10**3)
    except:
        pass


def input_calc_3(concrete_price_m40, concrete_price_m45, concrete_price_m60, concrete_gwp_m40,
               concrete_gwp_m45, concrete_gwp_m60, rebar_price, rebar_gwp, red_factor, stiffness,
               x, y, c_nom, k_dict, k_pick, iso_dict, iso_pick, iso_thickness, fiber_price, fiber_gwp):
    try:
        # User input
        df_3.loc[df_3['concrete_quality'] == 'B45 M40', 'concrete_price_input'] = float(concrete_price_m40.get())
        df_3.loc[df_3['concrete_quality'] == 'B35 M45', 'concrete_price_input'] = float(concrete_price_m45.get())
        df_3.loc[df_3['concrete_quality'] == 'B30 M60', 'concrete_price_input'] = float(concrete_price_m60.get())
        df_3['rebar_price_input'] = float(rebar_price.get())
        df_3.loc[df_3['concrete_quality'] == 'B45 M40', 'concrete_gwp_input'] = float(concrete_gwp_m40.get())
        df_3.loc[df_3['concrete_quality'] == 'B35 M45', 'concrete_gwp_input'] = float(concrete_gwp_m45.get())
        df_3.loc[df_3['concrete_quality'] == 'B30 M60', 'concrete_gwp_input'] = float(concrete_gwp_m60.get())
        df_3['rebar_gwp_input'] = float(rebar_gwp.get())
        df_3['fiber_price_input'] = float(fiber_price.get())
        df_3['fiber_gwp_input'] = float(fiber_gwp.get())
        df_3['reduction_factor_sigma_s2'] = float(red_factor.get())
        df_3['x'] = float(x.get())
        df_3['y'] = float(y.get())
        df_3['c_nom'] = float(c_nom.get())
        if len(k_pick.get()) == 0 or float(k_dict[k_pick.get()]) == 0:
            df_3['k'] = float(stiffness.get())
            if len(iso_pick.get()) == 0 or float(iso_dict[iso_pick.get()]) == 0 or float(iso_thickness.get()) == 0:
                df_3['k'] = float(stiffness.get())
            else:
                df_3['k'] = float(iso_dict[iso_pick.get()]) / float(iso_thickness.get())
        else:
            df_3['k'] = float(k_dict[k_pick.get()])
        # Calculations, filling the csv file with data
        df_3['rebar_price'] = df_3['rebar_price_input'] * df_3['rebar_per_square_meter_sum']
        df_3['concrete_price'] = df_3['concrete_price_input'] * df_3['concrete_per_square_meter']
        df_3['fiber_price'] = df_3['fiber_price_input'] * df_3['fiber_per_square_meter']
        df_3['price_sum'] = df_3['rebar_price'] + df_3['concrete_price'] + df_3['fiber_price']
        df_3['concrete_gwp'] = df_3['concrete_gwp_input'] * df_3['concrete_per_square_meter']
        df_3['rebar_gwp'] = df_3['rebar_gwp_input'] * df_3['rebar_per_square_meter_sum']
        df_3['fiber_gwp'] = df_3['fiber_gwp_input'] * df_3['fiber_per_square_meter']
        df_3['gwp_sum'] = df_3['concrete_gwp'] + df_3['rebar_gwp'] + df_3['fiber_gwp']
        df_3.loc[df_3['r'] < df_3['r_limit'], 'a'] = (1.6*df_3['r']**2+df_3['thickness']**2)**(1 / 2) - (0.675*df_3['thickness'])
        df_3.loc[df_3['r'] >= df_3['r_limit'], 'a'] = df_3['r']
        df_3.loc[df_3['reduction_factor_sigma_s2'] != 1, 'w_2'] = df_3['w'] * (df_3['reduction_factor_sigma_s2'])**2
        df_3.loc[df_3['reduction_factor_sigma_s2'] == 1, 'w_2'] = df_3['w']
        df_3['l_e'] = (df_3['capital_d'] / df_3['k'])**(1 / 4)
        df_3['westergaard_center'] = df_3['f_ck'] * df_3['thickness']**2 / (1.32 * np.log10(1.43 * df_3['l_e'] / df_3['a']))
        df_3['westergaard_edge'] = df_3['f_ck'] * df_3['thickness']**2 / (2.34 * np.log10(1.23 * df_3['l_e'] / df_3['a']))
        df_3['westergaard_corner'] = df_3['f_ck'] * df_3['thickness']**2 / (3 * (1 - (1.23 * (df_3['a'] / df_3['l_e'])**0.6)))
        df_3.loc[df_3['rebar_size_lower'] == 0, 'd_eff'] = df_3['c_nom'] + df_3['rebar_size_upper']
        df_3.loc[df_3['rebar_size_lower'] != 0, 'd_eff'] = df_3['thickness'] - df_3['c_nom'] - df_3['rebar_size_lower']
        df_3['ro_l'] = df_3['a_s_total'] / (df_3['d_eff'] * 1000)
        df_3['k_ec2'] = 1 + (200 / df_3['d_eff'])**(1 / 2)
        df_3.loc[df_3['k_ec2'] > 2, 'k_ec2'] = 2
        df_3['u_1_center'] = 2 * np.pi * (df_3['r'] + 2 * df_3['d_eff'])
        df_3['u_1_edge'] = np.pi * (df_3['r'] + 2 * df_3['d_eff'])
        df_3['u_1_corner'] = np.pi * (df_3['r'] + 2 * df_3['d_eff']) / 2
        df_3['c_rdc'] = 0.1
        df_3['v_rd'] = 0.75 * df_3['c_rdc'] * df_3['k_ec2'] * (100 * df_3['ro_l'] * df_3['f_ck'])**(1 / 3) + 0.6 * \
                       df_3['f_ftdr25'] * (df_3['a'] + df_3['d_eff']) / (df_3['a'] + 4 * df_3['d_eff'])
        df_3['v_min'] = 0.035 * df_3['k_ec2']**(3 / 2) * df_3['f_ck']**(1 / 2)
        df_3.loc[df_3['v_rd'] > df_3['v_min'], 'v_rd_2'] = df_3['v_rd']
        df_3.loc[df_3['v_rd'] <= df_3['v_min'], 'v_rd_2'] = df_3['v_min']
        df_3['v_ed_1_center'] = df_3['v_rd_2'] * df_3['u_1_center'] *df_3['d_eff']
        df_3['v_ed_1_edge'] = df_3['v_rd_2'] * df_3['u_1_edge'] *df_3['d_eff']
        df_3['v_ed_1_corner'] = df_3['v_rd_2'] * df_3['u_1_corner'] *df_3['d_eff']
        df_3['u_0_center'] = 2 * np.pi * df_3['r']
        df_3['u_0_edge'] = np.pi * df_3['r']
        df_3['u_0_corner'] = np.pi * df_3['r'] / 2
        df_3['v_ed_0_center'] = df_3['v_rd_max'] * df_3['u_0_center'] * df_3['d_eff']
        df_3['v_ed_0_edge'] = df_3['v_rd_max'] * df_3['u_0_edge'] * df_3['d_eff']
        df_3['v_ed_0_corner'] = df_3['v_rd_max'] * df_3['u_0_corner'] * df_3['d_eff']
        df_3['meyerhof_center'] = 6 * (1 + 2 * df_3['a'] / df_3['l_e']) * (df_3['m_p'] / 10**3 + df_3['m_n'] / 10**3
                                                                           + 2 * df_3['m_f'] / 10**3)
        df_3['meyerhof_edge'] = 3.5 * (1 + 3 * df_3['a'] / df_3['l_e']) * (df_3['m_p'] / 10**3 + df_3['m_n'] / 10**3
                                                                           + 2 * df_3['m_f'] / 10**3)
        df_3['meyerhof_corner'] = 2 * (1 + 4 * df_3['a'] / df_3['l_e']) * (df_3['m_n'] / 10**3 + df_3['m_f'] / 10**3)
        df_3['a_l_e_limit'] = df_3['a'] / df_3['l_e']
        df_3.loc[df_3['a_l_e_limit'] < 0.2, 'dual_point_load'] = (2 * np.pi + 1.8 * df_3['x'] / df_3['l_e']) * \
                                                             (df_3['m_p'] / 10**3 + df_3['m_n'] / 10**3 + 2 *
                                                              df_3['m_f'] / 10**3)
        df_3.loc[df_3['a_l_e_limit'] >= 0.2, 'dual_point_load'] = ((4 * np.pi / (1 - df_3['a'] / 3 * df_3['l_e'])) +
                                                              (1.8 * df_3['x'] / (df_3['l_e'] - df_3['a'] / 2))) * \
                                                              (df_3['m_p'] / 10**3 + df_3['m_n'] / 10**3 + 2 *
                                                               df_3['m_f'] / 10**3)
        df_3.loc[df_3['a_l_e_limit'] < 0.2, 'quadruple_point_load'] = (2 * np.pi + 1.8 * (df_3['x'] + df_3['y']) /
                                                                   df_3['l_e']) * (df_3['m_p'] / 10**3 + df_3['m_n'] /
                                                                                   10**3 + 2 * df_3['m_f'] / 10**3)
        df_3.loc[df_3['a_l_e_limit'] >= 0.2, 'quadruple_point_load'] = ((4 * np.pi / (1 - df_3['a'] / 3 * df_3['l_e'])) +
                                                                    (1.8 * (df_3['x'] + df_3['y']) /
                                                                     (df_3['l_e'] - df_3['a'] / 2))) * \
                                                                      (df_3['m_p'] / 10**3 + df_3['m_n'] / 10**3
                                                                       + 2 * df_3['m_f'] / 10**3)
    except:
        pass


def df_filtering(gk_pick, bk_pick, bk_dict, rebar_pick, rebar_dict, rv_pick, rv_dict, tykk_pick, tykk_dict, fast_pick):
    try:
        global df_temp
        if str(fast_pick.get()) == 'Fastholdt gulv':
            if len(str(gk_pick.get())) != 0 and str(gk_pick.get()) != 'Manuell inntasting' and len(rebar_pick.get()) != 0:
                gk_valg = int(gk_pick.get())
                gk_data = {1: {'riss': 0.3, 'as': 3, 't': 100, 'betong': 'B45 M40'},
                           2: {'riss': 0.5, 'as': 2, 't': 120, 'betong': 'B30 M60|B45 M40|B35 M45'},
                           3: {'riss': 1.0, 'as': 1, 't': 100, 'betong': 'B30 M60|B45 M40|B35 M45'},
                           4: {'riss': 100, 'as': 0, 't': 100, 'betong': 'B30 M60|B45 M40|B35 M45'}}
                df_temp = df[(df['thickness'] >= gk_data[gk_valg]['t']) &
                             (df['w_2'] <= gk_data[gk_valg]['riss']) &
                             (df['a_s_upper'] >= gk_data[gk_valg]['as'] * df['a_s_min']) &
                             (df['concrete_quality'].str.contains(gk_data[gk_valg]['betong'], case=False)) &
                             (df['rebar_size_upper'].isin(rebar_dict[rebar_pick.get()])) &
                             (df['rebar_size_lower'].isin(rebar_dict[rebar_pick.get()])) &
                             (df['a_s_total'] >= df['a_s_min'])]
            elif len(str(gk_pick.get())) == 0 or str(gk_pick.get()) == 'Manuell inntasting':
                df_temp = df[(df['concrete_quality'].str.contains(bk_dict[bk_pick.get()], case=False)) &
                             (df['rebar_size_upper'].isin(rebar_dict[rebar_pick.get()])) &
                             (df['rebar_size_lower'].isin(rebar_dict[rebar_pick.get()])) &
                             (df['w_2'] <= rv_dict[rv_pick.get()]) &
                             (df['thickness'].isin(tykk_dict[tykk_pick.get()])) &
                             (df['a_s_total'] >= df['a_s_min'])]
            else:
                tk.messagebox.showinfo('Feilmelding', 'Gulv egenskaper er ikke fylt ut!\n'
                                                      'Regler for utfylling av gulv-egenskaper:\n\nEnten:\n'
                                                      'Fyll ut gulvklasse OG ønsket armeringstype/størrelse'
                                                      '\nEller:\nFyll ut alle felt utenom gulvklasse for egendefinerte'
                                                      ' krav\n\nTips: Velg "Ingen krav" så vil alle valgene i menyen '
                                                      'velges!', master=window)
        elif str(fast_pick.get()) == 'Flytende gulv':
            if len(str(gk_pick.get())) != 0 and str(gk_pick.get()) != 'Manuell inntasting' and len(rebar_pick.get()) != 0:
                gk_valg = int(gk_pick.get())
                gk_data = {1: {'riss': 0.3, 'as': 3, 't': 100, 'betong': 'B45 M40'},
                           2: {'riss': 0.5, 'as': 2, 't': 120, 'betong': 'B30 M60|B45 M40|B35 M45'},
                           3: {'riss': 1.0, 'as': 1, 't': 100, 'betong': 'B30 M60|B45 M40|B35 M45'},
                           4: {'riss': 100, 'as': 0, 't': 100, 'betong': 'B30 M60|B45 M40|B35 M45'}}
                df_temp = df[(df['thickness'] >= gk_data[gk_valg]['t']) &
                             (df['a_s_upper'] >= gk_data[gk_valg]['as'] * df['a_s_min']) &
                             (df['concrete_quality'].str.contains(gk_data[gk_valg]['betong'], case=False)) &
                             (df['rebar_size_upper'].isin(rebar_dict[rebar_pick.get()])) &
                             (df['rebar_size_lower'].isin(rebar_dict[rebar_pick.get()])) &
                             (df['a_s_total'] >= df['a_s_min'])]
            elif len(str(gk_pick.get())) == 0 or str(gk_pick.get()) == 'Manuell inntasting':
                df_temp = df[(df['concrete_quality'].str.contains(bk_dict[bk_pick.get()], case=False)) &
                             (df['rebar_size_upper'].isin(rebar_dict[rebar_pick.get()])) &
                             (df['rebar_size_lower'].isin(rebar_dict[rebar_pick.get()])) &
                             (df['thickness'].isin(tykk_dict[tykk_pick.get()])) &
                             (df['a_s_total'] >= df['a_s_min'])]
            else:
                tk.messagebox.showinfo('Feilmelding', 'Gulv egenskaper er ikke fylt ut!\n'
                                                      'Regler for utfylling av gulv-egenskaper:\n\nEnten:\n'
                                                      'Fyll ut gulvklasse OG ønsket armeringstype/størrelse'
                                                      '\nEller:\nFyll ut alle felt utenom gulvklasse for egendefinerte'
                                                      ' krav\n\nTips: Velg "Ingen krav" så vil alle valgene i menyen '
                                                      'velges!', master=window)
        else:
            tk.messagebox.showinfo('Feilmelding', 'Forhold mellom gulv og grunn må fylles ut', master=window)
    except KeyError:
        tk.messagebox.showinfo('Feilmelding', '- Fyll inn alle felt \n- Bruk punktum som desimalskille'
                                              '\n- Utfyllbare felt skal bare inneholde tall',
                               master=window)


def df_2_filtering(gk_pick, bk_pick, bk_dict, rebar_pick, rebar_dict, rv_pick, rv_dict, tykk_pick, tykk_dict, fast_pick):
    try:
        global df_2_temp
        if str(fast_pick.get()) == 'Fastholdt gulv':
            if len(str(gk_pick.get())) != 0 and str(gk_pick.get()) != 'Manuell inntasting' and len(rebar_pick.get()) != 0:
                gk_valg = int(gk_pick.get())
                gk_data = {1: {'riss': 0.3, 'as': 3, 't': 100, 'betong': 'B45 M40'},
                           2: {'riss': 0.5, 'as': 2, 't': 120, 'betong': 'B30 M60|B45 M40|B35 M45'},
                           3: {'riss': 1.0, 'as': 1, 't': 100, 'betong': 'B30 M60|B45 M40|B35 M45'},
                           4: {'riss': 100, 'as': 0, 't': 100, 'betong': 'B30 M60|B45 M40|B35 M45'}}
                df_2_temp = df_2[(df_2['thickness'] >= gk_data[gk_valg]['t']) &
                             (df_2['w_2'] <= gk_data[gk_valg]['riss']) &
                             (df_2['a_s_upper'] >= gk_data[gk_valg]['as'] * df_2['a_s_min']) &
                             (df_2['concrete_quality'].str.contains(gk_data[gk_valg]['betong'], case=False)) &
                             (df_2['rebar_name_upper'].str.contains(rebar_dict[rebar_pick.get()])) &
                             (df_2['rebar_name_lower'].str.contains(rebar_dict[rebar_pick.get()])) &
                             (df_2['a_s_total'] >= df_2['a_s_min'])]
            elif len(str(gk_pick.get())) == 0 or str(gk_pick.get()) == 'Manuell inntasting':
                df_2_temp = df_2[(df_2['concrete_quality'].str.contains(bk_dict[bk_pick.get()], case=False)) &
                             (df_2['rebar_name_upper'].str.contains(rebar_dict[rebar_pick.get()])) &
                             (df_2['rebar_name_lower'].str.contains(rebar_dict[rebar_pick.get()])) &
                             (df_2['w_2'] <= rv_dict[rv_pick.get()]) &
                             (df_2['thickness'].isin(tykk_dict[tykk_pick.get()])) &
                             (df_2['a_s_total'] >= df_2['a_s_min'])]
            else:
                tk.messagebox.showinfo('Feilmelding', 'Armeringsnett er ikke fylt ut!', master=window)
        elif str(fast_pick.get()) == 'Flytende gulv':
            if len(str(gk_pick.get())) != 0 and str(gk_pick.get()) != 'Manuell inntasting' and len(rebar_pick.get()) != 0:
                gk_valg = int(gk_pick.get())
                gk_data = {1: {'riss': 0.3, 'as': 3, 't': 100, 'betong': 'B45 M40'},
                           2: {'riss': 0.5, 'as': 2, 't': 120, 'betong': 'B30 M60|B45 M40|B35 M45'},
                           3: {'riss': 1.0, 'as': 1, 't': 100, 'betong': 'B30 M60|B45 M40|B35 M45'},
                           4: {'riss': 100, 'as': 0, 't': 100, 'betong': 'B30 M60|B45 M40|B35 M45'}}
                df_2_temp = df_2[(df_2['thickness'] >= gk_data[gk_valg]['t']) &
                             (df_2['a_s_upper'] >= gk_data[gk_valg]['as'] * df_2['a_s_min']) &
                             (df_2['concrete_quality'].str.contains(gk_data[gk_valg]['betong'], case=False)) &
                             (df_2['rebar_name_upper'].str.contains(rebar_dict[rebar_pick.get()])) &
                             (df_2['rebar_name_lower'].str.contains(rebar_dict[rebar_pick.get()])) &
                             (df_2['a_s_total'] >= df_2['a_s_min'])]
            elif len(str(gk_pick.get())) == 0 or str(gk_pick.get()) == 'Manuell inntasting':
                df_2_temp = df_2[(df_2['concrete_quality'].str.contains(bk_dict[bk_pick.get()], case=False)) &
                             (df_2['rebar_name_upper'].str.contains(rebar_dict[rebar_pick.get()])) &
                             (df_2['rebar_name_lower'].str.contains(rebar_dict[rebar_pick.get()])) &
                             (df_2['thickness'].isin(tykk_dict[tykk_pick.get()])) &
                             (df_2['a_s_total'] >= df_2['a_s_min'])]
            else:
                tk.messagebox.showinfo('Feilmelding', 'Armeringsnett er ikke fylt ut!', master=window)
        else:
            pass
    except:
        pass


def df_3_filtering(gk_pick, bk_pick, bk_dict, rebar_pick, rebar_dict, rv_pick, rv_dict, tykk_pick, tykk_dict,
                   fast_pick, fiber_pick, fiber_dict, duct_pick, duct_dict):
    try:
        global df_3_temp
        if str(fast_pick.get()) == 'Fastholdt gulv':
            if len(str(gk_pick.get())) != 0 and str(gk_pick.get()) != 'Manuell inntasting' and len(rebar_pick.get()) != 0:
                gk_valg = int(gk_pick.get())
                gk_data = {1: {'riss': 0.3, 'as': 3, 't': 100, 'betong': 'B45 M40'},
                           2: {'riss': 0.5, 'as': 2, 't': 120, 'betong': 'B30 M60|B45 M40|B35 M45'},
                           3: {'riss': 1.0, 'as': 1, 't': 100, 'betong': 'B30 M60|B45 M40|B35 M45'},
                           4: {'riss': 100, 'as': 0, 't': 100, 'betong': 'B30 M60|B45 M40|B35 M45'}}
                df_3_temp = df_3[(df_3['thickness'] >= gk_data[gk_valg]['t']) &
                             (df_3['w_2'] <= gk_data[gk_valg]['riss']) &
                             (df_3['a_s_upper'] >= gk_data[gk_valg]['as'] * df_3['a_s_min']) &
                             (df_3['concrete_quality'].str.contains(gk_data[gk_valg]['betong'], case=False)) &
                             (df_3['rebar_size_upper'].isin(rebar_dict[rebar_pick.get()])) &
                             (df_3['rebar_size_lower'].isin(rebar_dict[rebar_pick.get()])) &
                             (df_3['f_r_1_k'].isin(fiber_dict[fiber_pick.get()])) &
                             (df_3['ductility'].str.contains(duct_dict[duct_pick.get()])) &
                             (df_3['a_s_total'] >= df_3['a_s_min'])]
            elif len(str(gk_pick.get())) == 0 or str(gk_pick.get()) == 'Manuell inntasting':
                df_3_temp = df_3[(df_3['concrete_quality'].str.contains(bk_dict[bk_pick.get()], case=False)) &
                             (df_3['rebar_size_upper'].isin(rebar_dict[rebar_pick.get()])) &
                             (df_3['rebar_size_lower'].isin(rebar_dict[rebar_pick.get()])) &
                             (df_3['f_r_1_k'].isin(fiber_dict[fiber_pick.get()])) &
                             (df_3['ductility'].str.contains(duct_dict[duct_pick.get()])) &
                             (df_3['w_2'] <= rv_dict[rv_pick.get()]) &
                             (df_3['thickness'].isin(tykk_dict[tykk_pick.get()])) &
                             (df_3['a_s_total'] >= df_3['a_s_min'])]
            else:
                tk.messagebox.showinfo('Feilmelding', 'Fiberarmerings klasse eller duktilitet er ikke fylt ut!',
                                       master=window)
        elif str(fast_pick.get()) == 'Flytende gulv':
            if len(str(gk_pick.get())) != 0 and str(gk_pick.get()) != 'Manuell inntasting' and len(rebar_pick.get()) != 0:
                gk_valg = int(gk_pick.get())
                gk_data = {1: {'riss': 0.3, 'as': 3, 't': 100, 'betong': 'B45 M40'},
                           2: {'riss': 0.5, 'as': 2, 't': 120, 'betong': 'B30 M60|B45 M40|B35 M45'},
                           3: {'riss': 1.0, 'as': 1, 't': 100, 'betong': 'B30 M60|B45 M40|B35 M45'},
                           4: {'riss': 100, 'as': 0, 't': 100, 'betong': 'B30 M60|B45 M40|B35 M45'}}
                df_3_temp = df_3[(df_3['thickness'] >= gk_data[gk_valg]['t']) &
                             (df_3['a_s_upper'] >= gk_data[gk_valg]['as'] * df_3['a_s_min']) &
                             (df_3['concrete_quality'].str.contains(gk_data[gk_valg]['betong'], case=False)) &
                             (df_3['rebar_size_upper'].isin(rebar_dict[rebar_pick.get()])) &
                             (df_3['rebar_size_lower'].isin(rebar_dict[rebar_pick.get()])) &
                             (df_3['f_r_1_k'].isin(fiber_dict[fiber_pick.get()])) &
                             (df_3['ductility'].str.contains(duct_dict[duct_pick.get()])) &
                             (df_3['a_s_total'] >= df_3['a_s_min'])]
            elif len(str(gk_pick.get())) == 0 or str(gk_pick.get()) == 'Manuell inntasting':
                df_3_temp = df_3[(df_3['concrete_quality'].str.contains(bk_dict[bk_pick.get()], case=False)) &
                             (df_3['rebar_size_upper'].isin(rebar_dict[rebar_pick.get()])) &
                             (df_3['rebar_size_lower'].isin(rebar_dict[rebar_pick.get()])) &
                             (df_3['f_r_1_k'].isin(fiber_dict[fiber_pick.get()])) &
                             (df_3['ductility'].str.contains(duct_dict[duct_pick.get()])) &
                             (df_3['thickness'].isin(tykk_dict[tykk_pick.get()])) &
                             (df_3['a_s_total'] >= df_3['a_s_min'])]
            else:
                tk.messagebox.showinfo('Feilmelding', 'Fiberarmerings klasse eller duktilitet er ikke fylt ut!',
                                       master=window)
        else:
            pass
    except:
        pass


def df_filtering_load(last_plassering_pick, lasttilfelle_pick):
    global df_temp2
    try:
        if last_plassering_pick.get() == 'Senter':
            if lasttilfelle_pick.get() == 'Single-point' or len(lasttilfelle_pick.get()) == 0:
                df_temp2 = df_temp[(df_temp['westergaard_center'] >= q_ed) & (df_temp['meyerhof_center'] >= q_ed * 1.5) &
                                   (df_temp['v_ed_1_center'] >= q_ed * 1.5) & (df_temp['v_ed_0_center'] >= q_ed * 1.5)]
            elif lasttilfelle_pick.get() == 'Dual-point':
                df_temp2 = df_temp[(df_temp['westergaard_center'] >= q_ed) & (df_temp['dual_point_load'] >= q_ed * 1.5) &
                                   (df_temp['v_ed_1_center'] >= q_ed * 1.5) & (df_temp['v_ed_0_center'] >= q_ed * 1.5) &
                                   (df_temp['meyerhof_center'] >= q_ed * 1.5)]
            elif lasttilfelle_pick.get() == 'Quadruple-point':
                df_temp2 = df_temp[(df_temp['westergaard_center'] >= q_ed) & (df_temp['quadruple_point_load'] >= q_ed * 1.5)
                                   & (df_temp['v_ed_1_center'] >= q_ed * 1.5) & (df_temp['v_ed_0_center'] >= q_ed * 1.5) &
                                   (df_temp['meyerhof_center'] >= q_ed * 1.5)]
        elif last_plassering_pick.get() == 'Kant':
            df_temp2 = df_temp[(df_temp['westergaard_edge'] >= q_ed) & (df_temp['meyerhof_edge'] >= q_ed * 1.5) &
                               (df_temp['v_ed_1_edge'] >= q_ed * 1.5) & (df_temp['v_ed_0_edge'] >= q_ed * 1.5)]
            if lasttilfelle_pick.get() == 'Dual-point' or lasttilfelle_pick.get() == 'Quadruple-point':
                tk.messagebox.showinfo('Feilmelding', 'Dual-point og quadruple-point lasttilfelle gjelder bare for last '
                                                      'plassert i senter!', master=window)
        elif last_plassering_pick.get() == 'Hjørne':
            df_temp2 = df_temp[(df_temp['westergaard_corner'] >= q_ed) & (df_temp['meyerhof_corner'] >= q_ed * 1.5) &
                               (df_temp['v_ed_1_corner'] >= q_ed * 1.5) & (df_temp['v_ed_0_corner'] >= q_ed * 1.5)]
            if lasttilfelle_pick.get() == 'Dual-point' or lasttilfelle_pick.get() == 'Quadruple-point':
                tk.messagebox.showinfo('Feilmelding', 'Dual-point og quadruple-point lasttilfelle gjelder bare for last '
                                                      'plassert i senter!', master=window)
        else:
            tk.messagebox.showinfo('Feilmelding', 'Last plassering må fylles ut!', master=window)
    except:
        tk.messagebox.showinfo('Feilmelding', 'Gulv egenskaper er ikke fylt ut!\nRegler for utfylling av '
                                              'gulv-egenskaper:\n\nEnten:\n'
                                              'Fyll ut gulvklasse OG ønsket armeringstype/størrelse'
                                              '\nEller:\nFyll ut alle felt utenom gulvklasse for egendefinerte'
                                              ' krav\n\nTips: Velg "Ingen krav" så vil alle valgene i menyen '
                                              'velges!', master=window)
    if q_ed == 0:
        tk.messagebox.showinfo('Feilmelding', 'Vennligst velg eller fyll ut dimensjonerende last!', master=window)


def df_2_filtering_load(last_plassering_pick, lasttilfelle_pick):
    global df_2_temp2
    try:
        if last_plassering_pick.get() == 'Senter':
            if lasttilfelle_pick.get() == 'Single-point' or len(lasttilfelle_pick.get()) == 0:
                df_2_temp2 = df_2_temp[(df_2_temp['westergaard_center'] >= q_ed) & (df_2_temp['meyerhof_center'] >= q_ed * 1.5) &
                                   (df_2_temp['v_ed_1_center'] >= q_ed * 1.5) & (df_2_temp['v_ed_0_center'] >= q_ed * 1.5)]
            elif lasttilfelle_pick.get() == 'Dual-point':
                df_2_temp2 = df_2_temp[(df_2_temp['westergaard_center'] >= q_ed) & (df_2_temp['dual_point_load'] >= q_ed * 1.5) &
                                   (df_2_temp['v_ed_1_center'] >= q_ed * 1.5) & (df_2_temp['v_ed_0_center'] >= q_ed * 1.5) &
                                   (df_2_temp['meyerhof_center'] >= q_ed * 1.5)]
            elif lasttilfelle_pick.get() == 'Quadruple-point':
                df_2_temp2 = df_2_temp[(df_2_temp['westergaard_center'] >= q_ed) & (df_2_temp['quadruple_point_load'] >= q_ed * 1.5)
                                   & (df_2_temp['v_ed_1_center'] >= q_ed * 1.5) & (df_2_temp['v_ed_0_center'] >= q_ed * 1.5) &
                                   (df_2_temp['meyerhof_center'] >= q_ed * 1.5)]
        elif last_plassering_pick.get() == 'Kant':
            df_2_temp2 = df_2_temp[(df_2_temp['westergaard_edge'] >= q_ed) & (df_2_temp['meyerhof_edge'] >= q_ed * 1.5) &
                               (df_2_temp['v_ed_1_edge'] >= q_ed * 1.5) & (df_2_temp['v_ed_0_edge'] >= q_ed * 1.5)]
        elif last_plassering_pick.get() == 'Hjørne':
            df_2_temp2 = df_2_temp[(df_2_temp['westergaard_corner'] >= q_ed) & (df_2_temp['meyerhof_corner'] >= q_ed * 1.5) &
                               (df_2_temp['v_ed_1_corner'] >= q_ed * 1.5) & (df_2_temp['v_ed_0_corner'] >= q_ed * 1.5)]
    except:
        pass


def df_sorting_price_gwp(sort_pick):
    try:
        global df_final
        if sort_pick.get() == 'Pris':
            df_final = df_temp2.sort_values(by='price_sum', ascending=True)
        elif sort_pick.get() == 'GWP':
            df_final = df_temp2.sort_values(by='gwp_sum', ascending=True)
        else:
            tk.messagebox.showinfo('Feilmelding', 'Sorterings kriteriet må fylles ut!', master=window)
    except NameError:
        print('test')


def df_2_sorting_price_gwp(sort_pick):
    global df_2_final
    try:
        if sort_pick.get() == 'Pris':
            df_2_final = df_2_temp2.sort_values(by='price_sum', ascending=True)
        elif sort_pick.get() == 'GWP':
            df_2_final = df_2_temp2.sort_values(by='gwp_sum', ascending=True)
    except:
        pass


def load_next_frames():
    if q_ed != 0 and 'check' in globals() and 'df_temp' in globals() and 'df_temp2' in globals() \
            and 'df_final' in globals() and 'df_2' in globals() and 'df_2_temp' in globals() and 'df_2_temp2' in globals()\
            and 'df_2_final' in globals():
        raise_frame(frame3, frame4)


def show_result():
    try:
        global tykkelse_resultat_df
        tykkelse_resultat_df = tk.Label(master=frame31, text=f'{df_final.iloc[0]["thickness"]}mm ', font=('Calibri', 11))
        tykkelse_resultat_df.grid(row=2, column=1, sticky='e')
        global armering_resultat_df
        armering_resultat_df = tk.Label(master=frame31, text=f'{df_final.iloc[0]["rebar_type"].split()[1].capitalize()}'
                                                             f' Ø {df_final.iloc[0]["rebar_size_upper"]} C '
                                                             f'{df_final.iloc[0]["cc_upper"]}mm ', font=('Calibri', 11))
        armering_resultat_df.grid(row=3, column=1, sticky='e')
        global betongkvalitet_resultat_df
        betongkvalitet_resultat_df = tk.Label(master=frame31, text=f'{df_final.iloc[0]["concrete_quality"]} ',
                                              font=('Calibri', 11))
        betongkvalitet_resultat_df.grid(row=4, column=1, sticky='e')
        global pris_resultat_df
        pris_resultat_df = tk.Label(master=frame31, text=f'{round(df_final.iloc[0]["price_sum"], 1)} NOK ',
                                    font=('Calibri', 11))
        pris_resultat_df.grid(row=5, column=1, sticky='e')
        global gwp_resultat_df
        gwp_resultat_df = tk.Label(master=frame31, text=f'{round(df_final.iloc[0]["gwp_sum"], 1)} kg CO2-eq ',
                                   font=('Calibri', 11))
        gwp_resultat_df.grid(row=6, column=1, sticky='e')
    except:
        pass


def show_result_2():
    try:
        global tykkelse_resultat_df_2
        tykkelse_resultat_df_2 = tk.Label(master=frame33, text=f'{df_2_final.iloc[0]["thickness"]}mm ', font=('Calibri', 11))
        tykkelse_resultat_df_2.grid(row=2, column=1, sticky='e')
        global armering_resultat_df_2
        armering_resultat_df_2 = tk.Label(master=frame33, text=f'{df_2_final.iloc[0]["rebar_type"].split()[1].capitalize()} '
                                                             f'{df_2_final.iloc[0]["rebar_name_upper"]} ', font=('Calibri', 11))
        armering_resultat_df_2.grid(row=3, column=1, sticky='e')
        global betongkvalitet_resultat_df_2
        betongkvalitet_resultat_df_2 = tk.Label(master=frame33, text=f'{df_2_final.iloc[0]["concrete_quality"]} ',
                                              font=('Calibri', 11))
        betongkvalitet_resultat_df_2.grid(row=4, column=1, sticky='e')
        global pris_resultat_df_2
        pris_resultat_df_2 = tk.Label(master=frame33, text=f'{round(df_2_final.iloc[0]["price_sum"], 1)} NOK ',
                                    font=('Calibri', 11))
        pris_resultat_df_2.grid(row=5, column=1, sticky='e')
        global gwp_resultat_df_2
        gwp_resultat_df_2 = tk.Label(master=frame33, text=f'{round(df_2_final.iloc[0]["gwp_sum"], 1)} kg CO2-eq ',
                                   font=('Calibri', 11))
        gwp_resultat_df_2.grid(row=6, column=1, sticky='e')
    except:
        pass


def clear_frames():
    try:
        # Frame 31
        tykkelse_resultat_df.destroy()
        armering_resultat_df.destroy()
        betongkvalitet_resultat_df.destroy()
        pris_resultat_df.destroy()
        gwp_resultat_df.destroy()
        # Frame 32
        tykkelse_resultat_df_2.destroy()
        armering_resultat_df_2.destroy()
        betongkvalitet_resultat_df_2.destroy()
        pris_resultat_df_2.destroy()
        gwp_resultat_df_2.destroy()
    except:
        pass


def get_df_value(dataf, arg):
    try:
        value = dataf.iloc[0][arg]
        return value
    except IndexError:
        value = 0
        return value


def raise_frame(f1, f2):
    f1.tkraise()
    f2.tkraise()


df = pd.read_csv('csv\\slakkarmering.csv', sep=';')
df_2 = pd.read_csv('csv\\nettarmering.csv', sep=';')
df_3 = pd.read_csv('csv\\slakk- + fiberarmering.csv', sep=';')

window = tk.Tk()
window.title('Beregningsverktøy - Gulv på grunn')
window.rowconfigure(0, weight=0)
window.columnconfigure(0, weight=0)

frame1 = tk.Frame(window)
# noinspection PyTypeChecker
frame1.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
                    minsize=35)
# noinspection PyTypeChecker
frame1.columnconfigure([0, 1, 2], minsize=250)

frame2 = tk.Frame(window)
# noinspection PyTypeChecker
frame2.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
                    minsize=35)
# noinspection PyTypeChecker
frame2.columnconfigure([0, 1], minsize=250)
frame2.columnconfigure(2, minsize=100)

frame3 = tk.Frame(window)
# noinspection PyTypeChecker
frame3.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
                    minsize=35)
# noinspection PyTypeChecker
frame3.columnconfigure([0, 1, 2], minsize=250)

frame4 = tk.Frame(window)
# noinspection PyTypeChecker
frame4.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21],
                    minsize=35)
# noinspection PyTypeChecker
frame4.columnconfigure([0, 1], minsize=250)
frame4.columnconfigure(2, minsize=100)

frame12 = tk.Frame(frame1)
# noinspection PyTypeChecker
frame12.columnconfigure([0, 2], minsize=40)

frame13 = tk.Frame(frame1)
# noinspection PyTypeChecker
frame13.columnconfigure([0, 1, 2], minsize=60)

frame14 = tk.Frame(frame1)
# noinspection PyTypeChecker
frame14.columnconfigure([0, 1], minsize=125)

frame22 = tk.Frame(frame2)
# noinspection PyTypeChecker
frame22.columnconfigure([0, 1, 2, 3, 4, 5], minsize=38)

frame23 = tk.Frame(frame2)
# noinspection PyTypeChecker
frame23.columnconfigure([0, 1, 2, 3, 4, 5], minsize=38)

raise_frame(frame1, frame2)

tk.Label()
# Creating labels for frame 1
fyll_inn_lbl = tk.Label(master=frame1, text='Vennligst legg inn gulvets ønskede egenskaper:', font=('Calibri', 12))
gulvklasse_lbl = tk.Label(master=frame1, text='Gulvklasse', font=('Calibri', 12))
bestandighetsklasse_lbl = tk.Label(master=frame1, text='Betongkvalitet', font=('Calibri', 12))
slakkarmeringsdiameter_lbl = tk.Label(master=frame1, text='Slakkarmeringsdiameter', font=('Calibri', 12))
armeringsnett_lbl = tk.Label(master=frame1, text='Armeringsnett', font=('Calibri', 12))
fiberarmering_lbl = tk.Label(master=frame1, text='Fiber restfasthetsklasse / duktilitet', font=('Calibri', 12))
duktilitet_lbl = tk.Label(master=frame14, text='Duktilitet', font=('Calibri', 12))
rissvidde_lbl = tk.Label(master=frame1, text='Rissvidde', font=('Calibri', 12))
tykkelse_lbl = tk.Label(master=frame1, text='Tykkelse', font=('Calibri', 12))
geometri_lbl = tk.Label(master=frame1, text='Geometri', font=('Calibri', 12))
fastholding_lbl = tk.Label(master=frame1, text='Forhold mellom gulv og grunn', font=('Calibri', 12))
dimensjonerende_last_lbl = tk.Label(master=frame1, text='Dimensjonerende last (Bare fyll ut den dimensjonerende)',
                                    font=('Calibri', 12))
gaffeltruck_klasse_lbl = tk.Label(master=frame1, text='Gaffeltruck-klasse', font=('Calibri', 12))
dekk_lbl = tk.Label(master=frame13, text='Dekk:', font=('Calibri', 12))
billast_lbl = tk.Label(master=frame1, text='Billast', font=('Calibri', 12))
nyttelast_lbl = tk.Label(master=frame1, text='Nyttelast', font=('Calibri', 12))
plassering_last_lbl = tk.Label(master=frame1, text='Last plassering', font=('Calibri', 12))
egendef_punktlast_lbl = tk.Label(master=frame1, text='Egendefinert punktlast', font=('Calibri', 12))
lastflate_lbl = tk.Label(master=frame1, text='Lastflatens radius (egendefinert last)', font=('Calibri', 12))
Lasttilfelle_egendef_punktlast_lbl = tk.Label(master=frame1, text='Lasttilfelle for egendefinert punktlast',
                                              font=('Calibri', 12))
gruppe_navn_lbl = tk.Label(master=frame1, text='© B22B02 - HIOF, i samarbeid med Multiconsult', font=('Calibri', 10))
rissvidde_enhet_lbl = tk.Label(master=frame1, text='mm', font=('Calibri', 12))
tykkelse_enhet_lbl = tk.Label(master=frame1, text='mm', font=('Calibri', 12))
lengde_enhet_lbl = tk.Label(master=frame1, text='m', font=('Calibri', 12))
bredde_enhet_lbl = tk.Label(master=frame1, text='m', font=('Calibri', 12))
egendef_punktlast_enhet_lbl = tk.Label(master=frame1, text='kN', font=('Calibri', 12))
lastflate_enhet_lbl = tk.Label(master=frame1, text='mm', font=('Calibri', 12))
avstand_mellom_punktlaster_lbl = tk.Label(master=frame1, text='Avstand mellom punktlaster',
                                          font=('Calibri', 12))
avstand_mellom_punktlaster_enhet_lbl = tk.Label(master=frame1, text='mm', font=('Calibri', 12))
x_lbl = tk.Label(master=frame12, text='X: ', font=('Calibri', 12))
y_lbl = tk.Label(master=frame12, text='Y: ', font=('Calibri', 12))
reduksjonsfaktor_lbl = tk.Label(master=frame1, text='Reduksjonsfaktor for armeringsspenning ',
                                font=('Calibri', 12))
nominell_overdekning_lbl = tk.Label(master=frame1, text='Nominell overdekning', font=('Calibri', 12))
nominell_overdekning_enhet_lbl = tk.Label(master=frame1, text='mm', font=('Calibri', 12))

# Creating option menu's for frame 1
gulvklasse_options = ['1', '2', '3', '4', 'Manuell inntasting']
gulvklasse_pick = tk.StringVar(frame1)
gulvklasse_option_menu = tk.OptionMenu(frame1, gulvklasse_pick, *gulvklasse_options)
bestandighetsklasse_options = ['B45 M40', 'B35 M45', 'B30 M60', 'Ingen krav']
bestandighetsklasse_pick = tk.StringVar(frame1)
bestandighetsklasse_option_menu = tk.OptionMenu(frame1, bestandighetsklasse_pick, *bestandighetsklasse_options)
bestandighetsklasse_dict = {'B45 M40': 'B45 M40', 'B35 M45': 'B35 M45|B45 M40', 'B30 M60': 'B30 M60|B35 M45|B45 M40',
                            'Ingen krav': 'B30 M60|B35 M45|B45 M40'}
slakkarmeringsdiameter_options = ['8', '10', '12', '14', '16', 'Ingen krav']
slakkarmeringsdiameter_pick = tk.StringVar(frame1)
slakkarmeringsdiameter_option_menu = tk.OptionMenu(frame1, slakkarmeringsdiameter_pick, *slakkarmeringsdiameter_options)
slakkarmeringsdiameter_dict = {'8': [8], '10': [10], '12': [12], '14': [14], '16': [16],
                               'Ingen krav': [8, 10, 12, 14, 16, 0]}
armeringsnett_options = ['K131', 'K189', 'K257', 'K335', 'K402', 'K503', 'Ingen krav']
armeringsnett_pick = tk.StringVar(frame1)
armeringsnett_option_menu = tk.OptionMenu(frame1, armeringsnett_pick, *armeringsnett_options)
armeringsnett_dict = {'K131': ['K131'], 'K189': ['K189'], 'K257': ['K257'], 'K335': ['K335'], 'K402': ['K402'],
                      'K503': ['K503'], 'Ingen krav': 'K131|K189|K257|K335|K402|K503|0'}
fiberarmering_options = ['2,0', '3,0', '4,0', '5,0', 'Ingen krav']
fiberarmering_pick = tk.StringVar(frame14)
fiberarmering_option_menu = tk.OptionMenu(frame14, fiberarmering_pick, *fiberarmering_options)
fiberarmering_dict = {'2,0': [2], '3,0': [3], '4,0': [4], '5,0': [5], 'Ingen krav': [2, 3, 4, 5]}
duktilitet_options = ['b', 'd', 'Ingen krav']
duktilitet_pick = tk.StringVar(frame14)
duktilitet_option_menu = tk.OptionMenu(frame14, duktilitet_pick, *duktilitet_options)
duktilitet_dict = {'b': ['b'], 'd': ['d'], 'Ingen krav': 'b|d'}
rissvidde_options = ['≤ 0,2', '≤ 0,3', '≤ 0,4', '≤ 0,5', '≤ 0,6', '≤ 0,7', '≤ 0,8', '≤ 0,9', '≤ 1,0', 'Ingen krav']
rissvidde_pick = tk.StringVar(frame1)
rissvidde_option_menu = tk.OptionMenu(frame1, rissvidde_pick, *rissvidde_options)
rissvidde_dict = {'≤ 0,2': 0.2, '≤ 0,3': 0.3, '≤ 0,4': 0.4, '≤ 0,5': 0.5, '≤ 0,6': 0.6, '≤ 0,7': 0.7, '≤ 0,8': 0.8,
                  '≤ 0,9': 0.9, '≤ 1,0': 1.0, 'Ingen krav': 100}
tykkelse_options = ['100', '110', '120', '130', '140', '150', '160', '170', '180', '190', '200', '210', '220', '230',
                    '240', '250', '260', '270', '280', '290', '300', 'Ingen krav']
tykkelse_pick = tk.StringVar(frame1)
tykkelse_option_menu = tk.OptionMenu(frame1, tykkelse_pick, *tykkelse_options)
tykkelse_dict = {'100': [100], '110': [110], '120': [120], '130': [130], '140': [140], '150': [150], '160': [160],
                 '170': [170], '180': [180], '190': [190], '200': [200], '210': [210], '220': [220], '230': [230],
                 '240': [240], '250': [250], '260': [260], '270': [270], '280': [280], '290': [290], '300': [300],
                 'Ingen krav': [110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270,
                                280, 290, 300]}
fastholding_options = ['Flytende gulv', 'Fastholdt gulv']
fastholding_pick = tk.StringVar(frame1)
fastholding_option_menu = tk.OptionMenu(frame1, fastholding_pick, *fastholding_options)
gaffeltruck_klasse_options = ['FL1', 'FL2', 'FL3', 'FL4', 'FL5', 'FL6', 'Ingen krav']
gaffeltruck_klasse_pick = tk.StringVar(frame13)
gaffeltruck_klasse_menu = tk.OptionMenu(frame13, gaffeltruck_klasse_pick, *gaffeltruck_klasse_options)
gaffeltruck_klasse_dict = {'FL1': 26, 'FL2': 40, 'FL3': 63, 'FL4': 90, 'FL5': 140, 'FL6': 170, 'Ingen krav': 0}
gaffeltruck_klasse_menu.config(width=8)
dekk_options = ['Luftfylt', 'Massiv']
dekk_pick = tk.StringVar(frame13)
dekk_menu = tk.OptionMenu(frame13, dekk_pick, *dekk_options)
dekk_dict = {'Luftfylt': 1.4, 'Massiv': 2.0}
dekk_menu.config(width=8)
billast_options = ['Kategori F', 'Kategori G', 'Ingen krav']
billast_pick = tk.StringVar(frame1)
billast_option_menu = tk.OptionMenu(frame1, billast_pick, *billast_options)
billast_dict = {'Kategori F': 20, 'Kategori G': 90, 'Ingen krav': 0}
nyttelast_options = ['Kategori A', 'Kategori B', 'Kategori C1', 'Kategori C2', 'Kategori C3', 'Kategori C4',
                     'Kategori C5', 'Kategori D1', 'Kategori D2', 'Kategori E', 'Ingen krav']
nyttelast_pick = tk.StringVar(frame1)
nyttelast_option_menu = tk.OptionMenu(frame1, nyttelast_pick, *nyttelast_options)
nyttelast_dict = {'Kategori A': 2, 'Kategori B': 2, 'Kategori C1': 4, 'Kategori C2': 4, 'Kategori C3': 4,
                  'Kategori C4': 7, 'Kategori C5': 4, 'Kategori D1': 4, 'Kategori D2': 7, 'Kategori E': 7,
                  'Ingen krav': 0}
plassering_last_options = ['Senter', 'Kant', 'Hjørne']
plassering_last_pick = tk.StringVar(frame1)
plassering_last_option_menu = tk.OptionMenu(frame1, plassering_last_pick, *plassering_last_options)
lasttilfelle_egendef_punktlast_options = ['Single-point', 'Dual-point', 'Quadruple-point']
lasttilfelle_egendef_punktlast_pick = tk.StringVar(frame1)
lasttilfelle_egendef_punktlast_menu = tk.OptionMenu(frame1, lasttilfelle_egendef_punktlast_pick,
                                                    *lasttilfelle_egendef_punktlast_options)

# Creating entries for frame 1
egendef_punktlast_pick = tk.StringVar(frame1)
egendef_punktlast_entry = tk.Entry(master=frame1, font=('Calibri', 12), textvariable=egendef_punktlast_pick)
egendef_punktlast_entry.insert(0, '0')
lastflate_pick = tk.StringVar(frame1)
lastflate_entry = tk.Entry(master=frame1, font=('Calibri', 12), textvariable=lastflate_pick)
lastflate_entry.insert(0, '0')
x_pick = tk.StringVar(frame12)
x_entry = tk.Entry(master=frame12, font=('Calibri', 12), textvariable=x_pick, width=8)
x_entry.insert(0, '0')
y_pick = tk.StringVar(frame12)
y_entry = tk.Entry(master=frame12, font=('Calibri', 12), textvariable=y_pick, width=8)
y_entry.insert(0, '0')
reduksjonsfaktor_pick = tk.StringVar(frame1)
reduksjonsfaktor_entry = tk.Entry(master=frame1, font=('Calibri', 12), textvariable=reduksjonsfaktor_pick)
reduksjonsfaktor_entry.insert(0, '1')
nominell_overdekning_pick = tk.StringVar(frame1)
nominell_overdekning_entry = tk.Entry(master=frame1, font=('Calibri', 12), textvariable=nominell_overdekning_pick)
nominell_overdekning_entry.insert(0, '0')

# Creating labels for frame 2
grunnforhold_lbl = tk.Label(master=frame2, text='Grunnforhold', font=('Calibri', 12))
isolasjon_lbl = tk.Label(master=frame2, text='Type isolasjon', font=('Calibri', 12))
isolasjon_tykkelse_lbl = tk.Label(master=frame2, text='Isolasjonstykkelse', font=('Calibri', 12))
grunnstivhet_lbl = tk.Label(master=frame2, text='Egendefinert k-verdi (grunnstivhet)', font=('Calibri', 12))
priser_lbl = tk.Label(master=frame2, text='Priser og miljøavtrykk', font=('Calibri', 12))
betong_pris_lbl = tk.Label(master=frame2, text='Betong pris', font=('Calibri', 12))
betong_pris_m40_lbl = tk.Label(master=frame22, text='M40', font=('Calibri', 12))
betong_pris_m45_lbl = tk.Label(master=frame22, text='M45', font=('Calibri', 12))
betong_pris_m60_lbl = tk.Label(master=frame22, text='M60', font=('Calibri', 12))
betong_gwp_lbl = tk.Label(master=frame2, text='Betong GWP', font=('Calibri', 12))
betong_gwp_m40_lbl = tk.Label(master=frame23, text='M40', font=('Calibri', 12))
betong_gwp_m45_lbl = tk.Label(master=frame23, text='M45', font=('Calibri', 12))
betong_gwp_m60_lbl = tk.Label(master=frame23, text='M60', font=('Calibri', 12))
slakkarmering_pris_lbl = tk.Label(master=frame2, text='Slakkarmering pris', font=('Calibri', 12))
slakkarmering_gwp_lbl = tk.Label(master=frame2, text='Slakkarmering GWP', font=('Calibri', 12))
nettarmering_pris_lbl = tk.Label(master=frame2, text='Nettarmering pris', font=('Calibri', 12))
nettarmering_gwp_lbl = tk.Label(master=frame2, text='Nettarmering GWP', font=('Calibri', 12))
fiberarmering_pris_gwp_lbl = tk.Label(master=frame2, text='Fiberarmering', font=('Calibri', 12))
staalfiber_pris_lbl = tk.Label(master=frame2, text='Stålfiber pris', font=('Calibri', 12))
staalfiber_gwp_lbl = tk.Label(master=frame2, text='Stålfiber GWP', font=('Calibri', 12))
isolasjon_tykkelse_enhet_lbl = tk.Label(master=frame2, text='mm', font=('Calibri', 12))
betong_pris_enhet_lbl = tk.Label(master=frame2, text='NOK / m^3', font=('Calibri', 12))
betong_gwp_enhet_lbl = tk.Label(master=frame2, text='kg CO2-eq / m^3', font=('Calibri', 12))
slakkarmering_pris_enhet_lbl = tk.Label(master=frame2, text='NOK / kg', font=('Calibri', 12))
slakkarmering_gwp_enhet_lbl = tk.Label(master=frame2, text='kg CO2-eq / kg', font=('Calibri', 12))
nettarmering_pris_enhet_lbl = tk.Label(master=frame2, text='NOK / kg', font=('Calibri', 12))
nettarmering_gwp_enhet_lbl = tk.Label(master=frame2, text='kg CO2-eq / kg', font=('Calibri', 12))
staalfiber_pris_enhet_lbl = tk.Label(master=frame2, text='NOK / kg', font=('Calibri', 12))
staalfiber_gwp_enhet_lbl = tk.Label(master=frame2, text='kg CO2-eq / kg', font=('Calibri', 12))
gulv_sortering_lbl = tk.Label(master=frame2, text='Sorter gulv etter:', font=('Calibri', 12))

# Creating option menus for frame 2
grunnforhold_options = ['Jordbunn', 'Lett komprimert sand', 'Godt komprimert sand', 'Våt leire', 'Tørr leire',
                        'Knust stein med sand', 'Grov knust stein', 'Godt komprimert knust stein',
                        'Egendefinert grunnstivhet']
grunnforhold_pick = tk.StringVar(frame2)
grunnforhold_option_menu = tk.OptionMenu(frame2, grunnforhold_pick, *grunnforhold_options)
grunnforhold_options_dict = {'Jordbunn': 0.015, 'Lett komprimert sand': 0.0225, 'Godt komprimert sand': 0.125,
                             'Våt leire': 0.045, 'Tørr leire': 0.09, 'Knust stein med sand': 0.125,
                             'Grov knust stein': 0.225, 'Godt komprimert knust stein': 0.25,
                             'Egendefinert grunnstivhet': 0}
isolasjon_options = ['EPS (300 kPa)', 'XPS (300 kPa)', 'Egendefinert grunnstivhet']
isolasjon_pick = tk.StringVar(frame2)
isolasjon_option_menu = tk.OptionMenu(frame2, isolasjon_pick, *isolasjon_options)
isolasjon_option_dict = {'EPS (300 kPa)': 6.0, 'XPS (300 kPa)': 12.0, 'Egendefinert grunnstivhet': 0}
gulv_sortering_options = ['Pris', 'GWP']
gulv_sortering_pick = tk.StringVar(frame2)
gulv_sortering_option_menu = tk.OptionMenu(frame2, gulv_sortering_pick, *gulv_sortering_options)

# Creating entries for frame 2
isolasjon_tykkelse_pick = tk.StringVar(frame2)
isolasjon_tykkelse_entry = tk.Entry(master=frame2, font=('Calibri', 12), textvariable=isolasjon_tykkelse_pick)
isolasjon_tykkelse_entry.insert(0, '0')
grunnstivhet_pick = tk.StringVar(frame2)
grunnstivhet_entry = tk.Entry(master=frame2, font=('Calibri', 12), textvariable=grunnstivhet_pick)
grunnstivhet_entry.insert(0, '0')
betong_pris_m40_pick = tk.StringVar(frame22)
betong_pris_m40_entry = tk.Entry(master=frame22, font=('Calibri', 12), textvariable=betong_pris_m40_pick, width=5)
betong_pris_m40_entry.insert(0, '1455')
betong_pris_m45_pick = tk.StringVar(frame22)
betong_pris_m45_entry = tk.Entry(master=frame22, font=('Calibri', 12), textvariable=betong_pris_m45_pick, width=5)
betong_pris_m45_entry.insert(0, '1355')
betong_pris_m60_pick = tk.StringVar(frame22)
betong_pris_m60_entry = tk.Entry(master=frame22, font=('Calibri', 12), textvariable=betong_pris_m60_pick, width=5)
betong_pris_m60_entry.insert(0, '1280')
betong_gwp_m40_pick = tk.StringVar(frame23)
betong_gwp_m40_entry = tk.Entry(master=frame23, font=('Calibri', 12), textvariable=betong_gwp_m40_pick, width=5)
betong_gwp_m40_entry.insert(0, '300')
betong_gwp_m45_pick = tk.StringVar(frame23)
betong_gwp_m45_entry = tk.Entry(master=frame23, font=('Calibri', 12), textvariable=betong_gwp_m45_pick, width=5)
betong_gwp_m45_entry.insert(0, '280')
betong_gwp_m60_pick = tk.StringVar(frame23)
betong_gwp_m60_entry = tk.Entry(master=frame23, font=('Calibri', 12), textvariable=betong_gwp_m60_pick, width=5)
betong_gwp_m60_entry.insert(0, '260')
slakkarmering_pris_pick = tk.StringVar(frame2)
slakkarmering_pris_entry = tk.Entry(master=frame2, font=('Calibri', 12), textvariable=slakkarmering_pris_pick)
slakkarmering_pris_entry.insert(0, '25')
slakkarmering_gwp_pick = tk.StringVar(frame2)
slakkarmering_gwp_entry = tk.Entry(master=frame2, font=('Calibri', 12), textvariable=slakkarmering_gwp_pick)
slakkarmering_gwp_entry.insert(0, '0.4')
nettarmering_pris_pick = tk.StringVar(frame2)
nettarmering_pris_entry = tk.Entry(master=frame2, font=('Calibri', 12), textvariable=nettarmering_pris_pick)
nettarmering_pris_entry.insert(0, '30')
nettarmering_gwp_pick = tk.StringVar(frame2)
nettarmering_gwp_entry = tk.Entry(master=frame2, font=('Calibri', 12), textvariable=nettarmering_gwp_pick)
nettarmering_gwp_entry.insert(0, '0.4')
staalfiber_pris_pick = tk.StringVar(frame2)
staalfiber_pris_entry = tk.Entry(master=frame2, font=('Calibri', 12), textvariable=staalfiber_pris_pick)
staalfiber_pris_entry.insert(0, '700')
staalfiber_gwp_pick = tk.StringVar(frame2)
staalfiber_gwp_entry = tk.Entry(master=frame2, font=('Calibri', 12), textvariable=staalfiber_gwp_pick)
staalfiber_gwp_entry.insert(0, '0.02')

# Creating frames for frame 3
frame31 = tk.Frame(master=frame3, bd=5, relief=tk.RAISED)
frame32 = tk.Frame(master=frame3, bd=5, relief=tk.RAISED)
frame33 = tk.Frame(master=frame3, bd=5, relief=tk.RAISED)
frame34 = tk.Frame(master=frame3, bd=5, relief=tk.RAISED)

# Row/column configure for frame 3 boxes
# noinspection PyTypeChecker
frame31.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], minsize=15)
# noinspection PyTypeChecker
frame31.columnconfigure(0, minsize=90)
frame31.columnconfigure(1, minsize=140)
# noinspection PyTypeChecker
frame32.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], minsize=15)
# noinspection PyTypeChecker
frame32.columnconfigure([0, 1], minsize=120)
# noinspection PyTypeChecker
frame33.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], minsize=15)
# noinspection PyTypeChecker
frame33.columnconfigure([0, 1], minsize=120)
# noinspection PyTypeChecker
frame34.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], minsize=15)
# noinspection PyTypeChecker
frame34.columnconfigure([0, 1], minsize=120)

# Creating labels for frame 3
resultat_lbl = tk.Label(master=frame3, text='Nedenfor vises de optimale gulvene basert på din input',
                        font=('Calibri', 12))
resultat2_lbl = tk.Label(master=frame3,
                         text='Trykk på "Rapport" for å få en utskrift med dokumentasjon for det gitte gulvet',
                         font=('Calibri', 12))
slakkarmering_resultat = tk.Label(master=frame31, text='Slakkarmering:', font=('Calibri', 11))
tykkelse_resultat = tk.Label(master=frame31, text='Tykkelse', font=('Calibri', 11))
armering_resultat = tk.Label(master=frame31, text='Armering', font=('Calibri', 11))
betongkvalitet_resultat = tk.Label(master=frame31, text='Betongkvalitet', font=('Calibri', 11))
pris_resultat = tk.Label(master=frame31, text='Pris ', font=('Calibri', 11))
gwp_resultat = tk.Label(master=frame31, text='GWP', font=('Calibri', 11))
slakkarmering_fib_resultat = tk.Label(master=frame32, text='Slakkarmering og', font=('Calibri', 11))
slakkarmering_fib_resultat2 = tk.Label(master=frame32, text='fiberarmering:', font=('Calibri', 11))
tykkelse2_resultat = tk.Label(master=frame32, text='Tykkelse', font=('Calibri', 11))
armering2_resultat = tk.Label(master=frame32, text='Armering', font=('Calibri', 11))
betongkvalitet2_resultat = tk.Label(master=frame32, text='Betongkvalitet', font=('Calibri', 11))
pris2_resultat = tk.Label(master=frame32, text='Pris ', font=('Calibri', 11))
gwp2_resultat = tk.Label(master=frame32, text='GWP', font=('Calibri', 11))
nettarmering_resultat = tk.Label(master=frame33, text='Nettarmering:', font=('Calibri', 11))
tykkelse3_resultat = tk.Label(master=frame33, text='Tykkelse', font=('Calibri', 11))
armering3_resultat = tk.Label(master=frame33, text='Armering', font=('Calibri', 11))
betongkvalitet3_resultat = tk.Label(master=frame33, text='Betongkvalitet', font=('Calibri', 11))
pris3_resultat = tk.Label(master=frame33, text='Pris ', font=('Calibri', 11))
gwp3_resultat = tk.Label(master=frame33, text='GWP', font=('Calibri', 11))
nettarmering_fib_resultat = tk.Label(master=frame34, text='Nettarmering og', font=('Calibri', 11))
nettarmering_fib_resultat2 = tk.Label(master=frame34, text='fiberarmering:', font=('Calibri', 11))
tykkelse4_resultat = tk.Label(master=frame34, text='Tykkelse', font=('Calibri', 11))
armering4_resultat = tk.Label(master=frame34, text='Armering', font=('Calibri', 11))
betongkvalitet4_resultat = tk.Label(master=frame34, text='Betongkvalitet', font=('Calibri', 11))
pris4_resultat = tk.Label(master=frame34, text='Pris ', font=('Calibri', 11))
gwp4_resultat = tk.Label(master=frame34, text='GWP', font=('Calibri', 11))
gruppe_navn_lbl2 = tk.Label(master=frame3, text='© B22B02 - HIOF, i samarbeid med Multiconsult', font=('Calibri', 10))

# Creating frames for frame 4
frame41 = tk.Frame(master=frame4, bd=5, relief=tk.RAISED)

# Row/column configure for frame 4 box
# noinspection PyTypeChecker
frame41.rowconfigure([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], minsize=15)
# noinspection PyTypeChecker
frame41.columnconfigure([0, 1], minsize=120)

# Creating labels for frame 4
fiberarmering_resultat = tk.Label(master=frame41, text='Fiberarmering:', font=('Calibri', 11))
tykkelse5_resultat = tk.Label(master=frame41, text='Tykkelse', font=('Calibri', 11))
armering5_resultat = tk.Label(master=frame41, text='Armering', font=('Calibri', 11))
betongkvalitet5_resultat = tk.Label(master=frame41, text='Betongkvalitet', font=('Calibri', 11))
pris5_resultat = tk.Label(master=frame41, text='Pris ', font=('Calibri', 11))
gwp5_resultat = tk.Label(master=frame41, text='GWP', font=('Calibri', 11))

# Frame 1 labels.grid
fyll_inn_lbl.grid(row=0, columnspan=2, sticky='w')
gulvklasse_lbl.grid(row=2, column=0, sticky='w')
bestandighetsklasse_lbl.grid(row=3, column=0, sticky='w')
slakkarmeringsdiameter_lbl.grid(row=4, column=0, sticky='w')
armeringsnett_lbl.grid(row=5, column=0, sticky='w')
fiberarmering_lbl.grid(row=6, column=0, sticky='w')
frame14.grid(row=6, column=1, sticky='news')
# duktilitet_lbl.grid(row=0, column=1, sticky='w')
rissvidde_lbl.grid(row=7, column=0, sticky='w')
tykkelse_lbl.grid(row=8, column=0, sticky='w')
fastholding_lbl.grid(row=9, column=0, sticky='w')
dimensjonerende_last_lbl.grid(row=10, column=0, sticky='w', columnspan=2)
gaffeltruck_klasse_lbl.grid(row=11, column=0, sticky='w')
frame13.grid(row=11, column=1)
dekk_lbl.grid(row=0, column=1)
billast_lbl.grid(row=12, column=0, sticky='w')
nyttelast_lbl.grid(row=13, column=0, sticky='w')
plassering_last_lbl.grid(row=14, column=0, sticky='w')
egendef_punktlast_lbl.grid(row=15, column=0, sticky='w')
lastflate_lbl.grid(row=16, column=0, sticky='w')
Lasttilfelle_egendef_punktlast_lbl.grid(row=17, column=0, sticky='w')
gruppe_navn_lbl.place(x=0, y=745)
rissvidde_enhet_lbl.grid(row=7, column=2, sticky='w')
tykkelse_enhet_lbl.grid(row=8, column=2, sticky='w')
egendef_punktlast_enhet_lbl.grid(row=15, column=2, sticky='w')
lastflate_enhet_lbl.grid(row=16, column=2, sticky='w')
avstand_mellom_punktlaster_lbl.grid(row=18, column=0, sticky='w')
avstand_mellom_punktlaster_enhet_lbl.grid(row=18, column=2, sticky='w')
frame12.grid(row=18, column=1)
x_lbl.grid(row=0, column=0, sticky='w')
y_lbl.grid(row=0, column=2, sticky='w')
reduksjonsfaktor_lbl.grid(row=19, column=0, sticky='w')
nominell_overdekning_lbl.grid(row=20, column=0, sticky='w')
nominell_overdekning_enhet_lbl.grid(row=20, column=2, sticky='w')

# Frame 1 optionmenu.grid
gulvklasse_option_menu.grid(row=2, column=1, sticky='ew')
bestandighetsklasse_option_menu.grid(row=3, column=1, sticky='ew')
slakkarmeringsdiameter_option_menu.grid(row=4, column=1, sticky='ew')
armeringsnett_option_menu.grid(row=5, column=1, sticky='ew')
fiberarmering_option_menu.grid(row=0, column=0, sticky='ew')
duktilitet_option_menu.grid(row=0, column=1, sticky='ew')
rissvidde_option_menu.grid(row=7, column=1, sticky='ew')
tykkelse_option_menu.grid(row=8, column=1, sticky='ew')
fastholding_option_menu.grid(row=9, column=1, sticky='ew')
gaffeltruck_klasse_menu.grid(row=0, column=0, sticky='ew')
dekk_menu.grid(row=0, column=2)
billast_option_menu.grid(row=12, column=1, sticky='ew')
nyttelast_option_menu.grid(row=13, column=1, sticky='ew')
plassering_last_option_menu.grid(row=14, column=1, sticky='ew')
lasttilfelle_egendef_punktlast_menu.grid(row=17, column=1, sticky='ew')

# Frame 1 entries.grid
egendef_punktlast_entry.grid(row=15, column=1, sticky='ew')
lastflate_entry.grid(row=16, column=1, sticky='ew')
x_entry.grid(row=0, column=1)
y_entry.grid(row=0, column=3)
reduksjonsfaktor_entry.grid(row=19, column=1, sticky='ew')
nominell_overdekning_entry.grid(row=20, column=1, sticky='ew')

# Frame 2 labels.grid
grunnforhold_lbl.grid(row=2, column=0, sticky='w')
isolasjon_lbl.grid(row=3, column=0, sticky='w')
isolasjon_tykkelse_lbl.grid(row=4, column=0, sticky='w')
grunnstivhet_lbl.grid(row=5, column=0, sticky='w')
priser_lbl.grid(row=7, column=0, sticky='w')
betong_pris_lbl.grid(row=8, column=0, sticky='w')
betong_gwp_lbl.grid(row=9, column=0, sticky='w')
slakkarmering_pris_lbl.grid(row=11, column=0, sticky='w')
slakkarmering_gwp_lbl.grid(row=12, column=0, sticky='w')
nettarmering_pris_lbl.grid(row=14, column=0, sticky='w')
nettarmering_gwp_lbl.grid(row=15, column=0, sticky='w')
staalfiber_pris_lbl.grid(row=17, column=0, sticky='w')
staalfiber_gwp_lbl.grid(row=18, column=0, sticky='w')
isolasjon_tykkelse_enhet_lbl.grid(row=4, column=2, sticky='w')
betong_pris_enhet_lbl.grid(row=8, column=2, sticky='w')
betong_gwp_enhet_lbl.grid(row=9, column=2, sticky='w')
frame22.grid(row=8, column=1)
frame23.grid(row=9, column=1)
betong_pris_m40_lbl.grid(row=0, column=0)
betong_pris_m45_lbl.grid(row=0, column=2)
betong_pris_m60_lbl.grid(row=0, column=4)
betong_gwp_m40_lbl.grid(row=0, column=0)
betong_gwp_m45_lbl.grid(row=0, column=2)
betong_gwp_m60_lbl.grid(row=0, column=4)
slakkarmering_pris_enhet_lbl.grid(row=11, column=2, sticky='w')
slakkarmering_gwp_enhet_lbl.grid(row=12, column=2, sticky='w')
nettarmering_pris_enhet_lbl.grid(row=14, column=2, sticky='w')
nettarmering_gwp_enhet_lbl.grid(row=15, column=2, sticky='w')
staalfiber_pris_enhet_lbl.grid(row=17, column=2, sticky='w')
staalfiber_gwp_enhet_lbl.grid(row=18, column=2, sticky='w')
gulv_sortering_lbl.grid(row=19, column=0, sticky='w')

# Frame 2 optionmenu.grid
grunnforhold_option_menu.grid(row=2, column=1, sticky='ew')
isolasjon_option_menu.grid(row=3, column=1, sticky='ew')
gulv_sortering_option_menu.grid(row=19, column=1, sticky='ew')

# Frame 2 entries.grid
isolasjon_tykkelse_entry.grid(row=4, column=1, sticky='ew')
grunnstivhet_entry.grid(row=5, column=1, sticky='ew')
betong_pris_m40_entry.grid(row=0, column=1)
betong_pris_m45_entry.grid(row=0, column=3)
betong_pris_m60_entry.grid(row=0, column=5)
betong_gwp_m40_entry.grid(row=0, column=1)
betong_gwp_m45_entry.grid(row=0, column=3)
betong_gwp_m60_entry.grid(row=0, column=5)
slakkarmering_pris_entry.grid(row=11, column=1, sticky='ew')
slakkarmering_gwp_entry.grid(row=12, column=1, sticky='ew')
nettarmering_pris_entry.grid(row=14, column=1, sticky='ew')
nettarmering_gwp_entry.grid(row=15, column=1, sticky='ew')
staalfiber_pris_entry.grid(row=17, column=1, sticky='ew')
staalfiber_gwp_entry.grid(row=18, column=1, sticky='ew')

# Frame 3 frame.grid
frame31.grid(row=3, rowspan=9, column=0, sticky='news', padx=10)
frame32.grid(row=13, rowspan=8, column=0, sticky='news', padx=10)
frame33.grid(row=3, rowspan=9, column=2, sticky='news')
frame34.grid(row=13, rowspan=8, column=2, sticky='news')

# Frame 3 label.grid
resultat_lbl.grid(row=0, column=0, columnspan=3, sticky='w')
resultat2_lbl.grid(row=1, column=0, columnspan=3, sticky='w')
slakkarmering_resultat.grid(row=0, column=0, sticky='w')
tykkelse_resultat.grid(row=2, column=0, stick='w')
armering_resultat.grid(row=3, column=0, stick='w')
betongkvalitet_resultat.grid(row=4, column=0, stick='w')
pris_resultat.grid(row=5, column=0, stick='w')
gwp_resultat.grid(row=6, column=0, stick='w')
slakkarmering_fib_resultat.grid(row=0, column=0, sticky='w')
slakkarmering_fib_resultat2.grid(row=1, column=0, sticky='w')
tykkelse2_resultat.grid(row=3, column=0, stick='w')
armering2_resultat.grid(row=4, column=0, stick='w')
betongkvalitet2_resultat.grid(row=5, column=0, stick='w')
pris2_resultat.grid(row=6, column=0, stick='w')
gwp2_resultat.grid(row=7, column=0, stick='w')
nettarmering_resultat.grid(row=0, column=0, sticky='w')
tykkelse3_resultat.grid(row=2, column=0, stick='w')
armering3_resultat.grid(row=3, column=0, stick='w')
betongkvalitet3_resultat.grid(row=4, column=0, stick='w')
pris3_resultat.grid(row=5, column=0, stick='w')
gwp3_resultat.grid(row=6, column=0, stick='w')
nettarmering_fib_resultat.grid(row=0, column=0, sticky='w')
nettarmering_fib_resultat2.grid(row=1, column=0, sticky='w')
tykkelse4_resultat.grid(row=3, column=0, stick='w')
armering4_resultat.grid(row=4, column=0, stick='w')
betongkvalitet4_resultat.grid(row=5, column=0, stick='w')
pris4_resultat.grid(row=6, column=0, stick='w')
gwp4_resultat.grid(row=7, column=0, stick='w')
gruppe_navn_lbl2.place(x=0, y=745)

# Frame 4 frame.grid
frame41.grid(row=3, rowspan=9, column=1, sticky='news', padx=5)

# Frame 4 label.grid
fiberarmering_resultat.grid(row=0, column=0, columnspan=3, sticky='w')
tykkelse5_resultat.grid(row=2, column=0, columnspan=3, sticky='w')
armering5_resultat.grid(row=3, column=0, columnspan=3, sticky='w')
betongkvalitet5_resultat.grid(row=4, column=0, columnspan=3, sticky='w')
pris5_resultat.grid(row=5, column=0, columnspan=3, sticky='w')
gwp5_resultat.grid(row=6, column=0, columnspan=3, sticky='w')

# Frontpage button
fortsett_btn = tk.Button(master=frame2, text='Fortsett', font=('Calibri', 14), padx=25, pady=8,
                         command=lambda: [loads(gaffeltruck_klasse_pick, gaffeltruck_klasse_dict, dekk_pick, dekk_dict,
                                                billast_pick, billast_dict, nyttelast_pick, nyttelast_dict,
                                                egendef_punktlast_pick, lastflate_pick),
                                          loads_2(gaffeltruck_klasse_pick, gaffeltruck_klasse_dict, dekk_pick, dekk_dict,
                                                  billast_pick, billast_dict, nyttelast_pick, nyttelast_dict,
                                                  egendef_punktlast_pick, lastflate_pick),
                                          loads_3(gaffeltruck_klasse_pick, gaffeltruck_klasse_dict, dekk_pick, dekk_dict,
                                                  billast_pick, billast_dict, nyttelast_pick, nyttelast_dict,
                                                  egendef_punktlast_pick, lastflate_pick),
                                          input_calc(betong_pris_m40_pick, betong_pris_m45_pick, betong_pris_m60_pick,
                                                     betong_gwp_m40_pick, betong_gwp_m45_pick, betong_gwp_m60_pick,
                                                     slakkarmering_pris_pick,
                                                     slakkarmering_gwp_pick, reduksjonsfaktor_pick,
                                                     grunnstivhet_pick, x_pick, y_pick,
                                                     nominell_overdekning_pick, grunnforhold_options_dict,
                                                     grunnforhold_pick, isolasjon_option_dict, isolasjon_pick,
                                                     isolasjon_tykkelse_pick),
                                          input_calc_2(betong_pris_m40_pick, betong_pris_m45_pick, betong_pris_m60_pick,
                                                       betong_gwp_m40_pick, betong_gwp_m45_pick, betong_gwp_m60_pick,
                                                       nettarmering_pris_pick,
                                                       nettarmering_gwp_pick, reduksjonsfaktor_pick,
                                                       grunnstivhet_pick, x_pick, y_pick,
                                                       nominell_overdekning_pick, grunnforhold_options_dict,
                                                       grunnforhold_pick, isolasjon_option_dict, isolasjon_pick,
                                                       isolasjon_tykkelse_pick),
                                          input_calc_3(betong_pris_m40_pick, betong_pris_m45_pick, betong_pris_m60_pick,
                                                       betong_gwp_m40_pick, betong_gwp_m45_pick, betong_gwp_m60_pick,
                                                       nettarmering_pris_pick,
                                                       nettarmering_gwp_pick, reduksjonsfaktor_pick,
                                                       grunnstivhet_pick, x_pick, y_pick,
                                                       nominell_overdekning_pick, grunnforhold_options_dict,
                                                       grunnforhold_pick, isolasjon_option_dict, isolasjon_pick,
                                                       isolasjon_tykkelse_pick, staalfiber_pris_pick, staalfiber_gwp_pick),
                                          df_filtering(gulvklasse_pick, bestandighetsklasse_pick,
                                                       bestandighetsklasse_dict,
                                                       slakkarmeringsdiameter_pick, slakkarmeringsdiameter_dict,
                                                       rissvidde_pick, rissvidde_dict,
                                                       tykkelse_pick, tykkelse_dict, fastholding_pick),
                                          df_2_filtering(gulvklasse_pick, bestandighetsklasse_pick,
                                                         bestandighetsklasse_dict,
                                                         armeringsnett_pick, armeringsnett_dict,
                                                         rissvidde_pick, rissvidde_dict,
                                                         tykkelse_pick, tykkelse_dict, fastholding_pick),
                                          df_3_filtering(gulvklasse_pick, bestandighetsklasse_pick,
                                                         bestandighetsklasse_dict,
                                                         slakkarmeringsdiameter_pick, slakkarmeringsdiameter_dict,
                                                         rissvidde_pick, rissvidde_dict,
                                                         tykkelse_pick, tykkelse_dict, fastholding_pick,
                                                         fiberarmering_pick, fiberarmering_dict, duktilitet_pick,
                                                         duktilitet_dict),
                                          df_filtering_load(plassering_last_pick, lasttilfelle_egendef_punktlast_pick),
                                          df_2_filtering_load(plassering_last_pick, lasttilfelle_egendef_punktlast_pick),
                                          df_sorting_price_gwp(gulv_sortering_pick),
                                          df_2_sorting_price_gwp(gulv_sortering_pick),
                                          load_next_frames(),
                                          show_result(),
                                          show_result_2()])
# raise_frame(frame3, frame4)
fortsett_btn.place(x=260, y=700)
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
frame3.grid(row=0, column=0, sticky='news')
frame4.grid(row=0, column=1, sticky='news')

# Result buttons
resultat1_btn = tk.Button(master=frame31, text='Rapport', font=('Calibri', 14), padx=40, pady=5,
                          command=lambda: [
                              create_pdf(
                                  tittel='Rapport for slakkarmert gulv på grunn.pdf',
                                  tykkelse=get_df_value(df_final, "thickness"),
                                  betong=get_df_value(df_final, "concrete_quality"),
                                  armeringstype=get_df_value(df_final, "rebar_type"),
                                  senteravstand=get_df_value(df_final, "cc"),
                                  last=q_ed,
                                  grunnstivhet=get_df_value(df_final, "k"),
                                  radius=get_df_value(df_final, "r"),
                                  overdekning=get_df_value(df_final, "c_nom"),
                                  x=get_df_value(df_final, "x"),
                                  y=get_df_value(df_final, "y"),
                                  l_b=get_df_value(df_final, "l_b"),
                                  sigma_s2=get_df_value(df_final, "sigma_s2"),
                                  e_s=get_df_value(df_final, "rebar_e_modulus"),
                                  rebar_size=get_df_value(df_final, "rebar_size"),
                                  f_ctm=get_df_value(df_final, "f_ctm"),
                                  a_c=get_df_value(df_final, "a_c"),
                                  a_s=get_df_value(df_final, "a_s"),
                                  w=get_df_value(df_final, "w_2"),
                                  f_ck=get_df_value(df_final, "f_ck"),
                                  l_e=get_df_value(df_final, "l_e"),
                                  a=get_df_value(df_final, "a"),
                                  westergaard_senter=get_df_value(df_final, "westergaard_center"),
                                  westergaard_kant=get_df_value(df_final, "westergaard_edge"),
                                  westergaard_hjorne=get_df_value(df_final, "westergaard_corner"),
                                  stor_d=get_df_value(df_final, "capital_d"),
                                  e_cm=get_df_value(df_final, "concrete_e_modulus"),
                                  m_n=get_df_value(df_final, "m_n"),
                                  m_p=get_df_value(df_final, "m_p"),
                                  meyerhof_senter=get_df_value(df_final, "meyerhof_center"),
                                  meyerhof_kant=get_df_value(df_final, "meyerhof_edge"),
                                  meyerhof_hjorne=get_df_value(df_final, "meyerhof_corner"),
                                  d_eff=get_df_value(df_final, "d_eff"),
                                  z=get_df_value(df_final, "z"),
                                  rho=get_df_value(df_final, "ro_l"),
                                  dual_point=get_df_value(df_final, "dual_point_load"),
                                  quadruple_point=get_df_value(df_final, "quadruple_point_load"),
                                  v_rd_2=get_df_value(df_final, "v_rd_2"),
                                  u_1_senter=get_df_value(df_final, "u_1_center"),
                                  u_1_kant=get_df_value(df_final, "u_1_edge"),
                                  u_1_hjorne=get_df_value(df_final, "u_1_corner"),
                                  v_ed_1_senter=get_df_value(df_final, "v_ed_1_center"),
                                  v_ed_1_kant=get_df_value(df_final, "v_ed_1_edge"),
                                  v_ed_1_hjorne=get_df_value(df_final, "v_ed_1_corner"),
                                  c_rdc=get_df_value(df_final, "c_rdc"),
                                  v_min=get_df_value(df_final, "v_min"),
                                  k_ec2=get_df_value(df_final, "k_ec2"),
                                  v_rd_max=get_df_value(df_final, "v_rd_max"),
                                  v_ed_0_senter=get_df_value(df_final, "v_ed_0_center"),
                                  v_ed_0_kant=get_df_value(df_final, "v_ed_0_edge"),
                                  v_ed_0_hjorne=get_df_value(df_final, "v_ed_0_corner"),
                                  u_0_senter=get_df_value(df_final, "u_0_center"),
                                  u_0_kant=get_df_value(df_final, "u_0_edge"),
                                  u_0_hjorne=get_df_value(df_final, "u_0_corner"),
                                  v_2=get_df_value(df_final, "v_2"),
                                  f_cd=get_df_value(df_final, "f_cd"),
                                  a_s_min=get_df_value(df_final, "a_s_min"),
                                  reduksjonsfaktor=get_df_value(df_final, "reduction_factor_sigma_s2"),
                                  as_per_square_meter=get_df_value(df_final, 'rebar_per_square_meter_sum'),
                                  concrete_per_square_meter=get_df_value(df_final, 'concrete_per_square_meter'),
                                  rebar_price_input=get_df_value(df_final, 'rebar_price_input'),
                                  concrete_price_input=get_df_value(df_final, 'concrete_price_input'),
                                  rebar_gwp_input=get_df_value(df_final, 'rebar_gwp_input'),
                                  concrete_gwp_input=get_df_value(df_final, 'concrete_gwp_input'),
                                  price_sum=get_df_value(df_final, 'price_sum'),
                                  gwp_sum=get_df_value(df_final, 'gwp_sum'),
                                  gulvklasse=gulvklasse_pick.get(),
                                  f_ctd=get_df_value(df_final, 'f_ctd'),
                                  fastholding=fastholding_pick.get(),
                                  lastplassering=plassering_last_pick.get()
                              )
                          ])
resultat2_btn = tk.Button(master=frame32, text='Rapport', font=('Calibri', 14), padx=40, pady=5)
resultat3_btn = tk.Button(master=frame33, text='Rapport', font=('Calibri', 14), padx=40, pady=5,
                          command=lambda: [
                              create_pdf(
                                  tittel='Rapport for nettarmert gulv på grunn.pdf',
                                  tykkelse=get_df_value(df_2_final, "thickness"),
                                  betong=get_df_value(df_2_final, "concrete_quality"),
                                  armeringstype=get_df_value(df_2_final, "rebar_type"),
                                  senteravstand=get_df_value(df_2_final, "cc"),
                                  last=q_ed,
                                  grunnstivhet=get_df_value(df_2_final, "k"),
                                  radius=get_df_value(df_2_final, "r"),
                                  overdekning=get_df_value(df_2_final, "c_nom"),
                                  x=get_df_value(df_2_final, "x"),
                                  y=get_df_value(df_2_final, "y"),
                                  l_b=get_df_value(df_2_final, "l_b"),
                                  sigma_s2=get_df_value(df_2_final, "sigma_s2"),
                                  e_s=get_df_value(df_2_final, "rebar_e_modulus"),
                                  rebar_size=get_df_value(df_2_final, "rebar_size"),
                                  f_ctm=get_df_value(df_2_final, "f_ctm"),
                                  a_c=get_df_value(df_2_final, "a_c"),
                                  a_s=get_df_value(df_2_final, "a_s"),
                                  w=get_df_value(df_2_final, "w_2"),
                                  f_ck=get_df_value(df_2_final, "f_ck"),
                                  l_e=get_df_value(df_2_final, "l_e"),
                                  a=get_df_value(df_2_final, "a"),
                                  westergaard_senter=get_df_value(df_2_final, "westergaard_center"),
                                  westergaard_kant=get_df_value(df_2_final, "westergaard_edge"),
                                  westergaard_hjorne=get_df_value(df_2_final, "westergaard_corner"),
                                  stor_d=get_df_value(df_2_final, "capital_d"),
                                  e_cm=get_df_value(df_2_final, "concrete_e_modulus"),
                                  m_n=get_df_value(df_2_final, "m_n"),
                                  m_p=get_df_value(df_2_final, "m_p"),
                                  meyerhof_senter=get_df_value(df_2_final, "meyerhof_center"),
                                  meyerhof_kant=get_df_value(df_2_final, "meyerhof_edge"),
                                  meyerhof_hjorne=get_df_value(df_2_final, "meyerhof_corner"),
                                  d_eff=get_df_value(df_2_final, "d_eff"),
                                  z=get_df_value(df_2_final, "z"),
                                  rho=get_df_value(df_2_final, "ro_l"),
                                  dual_point=get_df_value(df_2_final, "dual_point_load"),
                                  quadruple_point=get_df_value(df_2_final, "quadruple_point_load"),
                                  v_rd_2=get_df_value(df_2_final, "v_rd_2"),
                                  u_1_senter=get_df_value(df_2_final, "u_1_center"),
                                  u_1_kant=get_df_value(df_2_final, "u_1_edge"),
                                  u_1_hjorne=get_df_value(df_2_final, "u_1_corner"),
                                  v_ed_1_senter=get_df_value(df_2_final, "v_ed_1_center"),
                                  v_ed_1_kant=get_df_value(df_2_final, "v_ed_1_edge"),
                                  v_ed_1_hjorne=get_df_value(df_2_final, "v_ed_1_corner"),
                                  c_rdc=get_df_value(df_2_final, "c_rdc"),
                                  v_min=get_df_value(df_2_final, "v_min"),
                                  k_ec2=get_df_value(df_2_final, "k_ec2"),
                                  v_rd_max=get_df_value(df_2_final, "v_rd_max"),
                                  v_ed_0_senter=get_df_value(df_2_final, "v_ed_0_center"),
                                  v_ed_0_kant=get_df_value(df_2_final, "v_ed_0_edge"),
                                  v_ed_0_hjorne=get_df_value(df_2_final, "v_ed_0_corner"),
                                  u_0_senter=get_df_value(df_2_final, "u_0_center"),
                                  u_0_kant=get_df_value(df_2_final, "u_0_edge"),
                                  u_0_hjorne=get_df_value(df_2_final, "u_0_corner"),
                                  v_2=get_df_value(df_2_final, "v_2"),
                                  f_cd=get_df_value(df_2_final, "f_cd"),
                                  a_s_min=get_df_value(df_2_final, "a_s_min"),
                                  reduksjonsfaktor=get_df_value(df_2_final, "reduction_factor_sigma_s2"),
                                  as_per_square_meter=get_df_value(df_2_final, 'rebar_per_square_meter_sum'),
                                  concrete_per_square_meter=get_df_value(df_2_final, 'concrete_per_square_meter'),
                                  rebar_price_input=get_df_value(df_2_final, 'rebar_price_input'),
                                  concrete_price_input=get_df_value(df_2_final, 'concrete_price_input'),
                                  rebar_gwp_input=get_df_value(df_2_final, 'rebar_gwp_input'),
                                  concrete_gwp_input=get_df_value(df_2_final, 'concrete_gwp_input'),
                                  price_sum=get_df_value(df_2_final, 'price_sum'),
                                  gwp_sum=get_df_value(df_2_final, 'gwp_sum'),
                                  gulvklasse=gulvklasse_pick.get(),
                                  armeringsnavn=get_df_value(df_2_final, 'rebar_name'),
                                  f_ctd=get_df_value(df_2_final, 'f_ctd'),
                                  fastholding=fastholding_pick.get(),
                                  lastplassering=plassering_last_pick.get()
                              )
                          ])
resultat4_btn = tk.Button(master=frame34, text='Rapport', font=('Calibri', 14), padx=40, pady=5)
resultat5_btn = tk.Button(master=frame41, text='Rapport', font=('Calibri', 14), padx=40, pady=5)
tilbake_btn = tk.Button(master=frame4, text='Tilbake  ', font=('Calibri', 14), padx=25, pady=8,
                        command=lambda: [raise_frame(frame1, frame2), clear_frames()])
resultat1_btn.grid(row=10, columnspan=2)
resultat2_btn.grid(row=10, columnspan=2)
resultat3_btn.grid(row=10, columnspan=2)
resultat4_btn.grid(row=10, columnspan=2)
resultat5_btn.grid(row=10, columnspan=2)
tilbake_btn.place(x=260, y=700)

window.mainloop()

df_temp.to_csv('Steg 11.csv', sep=';')
df_2_temp.to_csv('Steg 12.csv', sep=';')
df_3_temp.to_csv('Steg 13.csv', sep=';')
#df_2_temp.to_csv('Steg 2.csv', sep=';')
#df_2_temp2.to_csv('Steg 3.csv', sep=';')
#df_2_final.to_csv('Final.csv', sep=';')
