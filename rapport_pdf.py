import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import tkinter.messagebox

def create_pdf(tittel='Rapport.pdf', tykkelse=0, betong=0, armeringstype=0, senteravstand=0, last=0,
               grunnstivhet=0, radius=0, reduksjonsfaktor=0, overdekning=0, x=0, y=0, l_b=0, sigma_s2=0, e_s=0,
               rebar_size=0, f_ctm=0, a_c=0, a_s=0, w=0, f_ck=0, l_e=1, a=1, westergaard_senter=0, westergaard_kant=0,
               westergaard_hjorne=0, stor_d=0, e_cm=0, m_n=0, m_p=0, meyerhof_senter=0, meyerhof_kant=0,
               meyerhof_hjorne=0, d_eff=0, z=0, rho=0, dual_point=0,
               quadruple_point=0, v_rd_2=0, u_1_senter=0, u_1_kant=0, u_1_hjorne=0, v_ed_1_senter=0,
               v_ed_1_kant=0, v_ed_1_hjorne=0, c_rdc=0, v_min=0, k_ec2=0, v_rd_max=0, v_ed_0_senter=0,
               v_ed_0_kant=0, v_ed_0_hjorne=0, u_0_senter=0, u_0_kant=0, u_0_hjorne=0, v_2=0, f_cd=0, a_s_min=1,
               as_per_square_meter=0, concrete_per_square_meter=0, rebar_price_input=0, concrete_price_input=0,
               rebar_gwp_input=0, concrete_gwp_input=0, price_sum=0, gwp_sum=0, gulvklasse=0, armeringsnavn=0, f_ctd=0,
               fastholding=0, lastplassering=0):
    try:
        c = canvas.Canvas(tittel, bottomup=0)

        linje1 = c.beginText()
        linje1.setTextOrigin(20 * mm, 20 * mm)
        linje1.setFont('Helvetica', 12)

        if armeringstype == 'nettarmering enkel' or armeringstype == 'nettarmering dobbel':
            linje1_name = 'Nettarmeringstype'
            linje1_name2 = f'{armeringsnavn}'
        else:
            linje1_name = ''
            linje1_name2 = ''

        if fastholding == 'Fastholdt gulv':
            riss11 = 'w'
            riss12 = ''
            riss13 = ''
            riss14 = 'l_b'
            riss15 = ''
            riss16 = ''
            riss17 = 'sigma_s2'
            riss21 = '= l_b * sigma_s2 / E_s'
            riss22 = f'= {round(l_b, 2)} * {round(sigma_s2, 2)} / {e_s}'
            riss23 = ''
            riss24 = '= sigma_s2 * Ø / ( 7.2 * f_ctm )'
            riss25 = f'= {round(sigma_s2, 2)} * {rebar_size} / ( 7.2 * {f_ctm} )'
            riss26 = ''
            riss27 = '= A_c * 0.8 * f_ctm * b / A_s'
            riss28 = f'= {a_c} * 0.8 * {f_ctm} * {reduksjonsfaktor} / {round(a_s, 2)}'
            riss31 = f'= {round(w, 4)} mm'
            riss32 = ''
            riss33 = ''
            riss34 = f'= {round(l_b, 2)} mm'
            riss35 = ''
            riss36 = ''
            riss37 = f'= {round(sigma_s2, 2)} N/mm^2'
        else:
            riss11 = 'For flytende gulv: Kontroll av rissvidde er OK hvis A_s tilfredstiller kravene til gulvklassen.'
            riss12 = ''
            riss13 = 'Forhold mellom A_s og A_s,min finnes på side 4 i rapporten.'
            riss14 = ''
            riss15 = ''
            riss16 = ''
            riss17 = ''
            riss21 = ''
            riss22 = ''
            riss23 = ''
            riss24 = ''
            riss25 = ''
            riss26 = ''
            riss27 = ''
            riss28 = ''
            riss31 = ''
            riss32 = ''
            riss33 = ''
            riss34 = ''
            riss35 = ''
            riss36 = ''
            riss37 = ''

        linje1_text = [
            'Rapport',
            '',
            '',
            'Input:',
            '',
            'Tykkelse:',
            'Betongkvalitet:',
            'Armeringstype',
            'Armeringsstørrelse',
            'Senteravstand',
            'Gulvklasse',
            linje1_name,
            '',
            '',
            '',
            'Kontroll i bruksgrensetilstand:',
            '',
            'Spenningsbegrensning, Westergaard:',
            '',
            'P_max,senter',
            '',
            '',
            'P_max,kant',
            '',
            '',
            'P_max,hjørne',
            '',
            '',
            '',
            'a',
            '',
            '',
            'l_e',
            '',
            '',
            'D',
            '',
            '',
            'Rissvidde:',
            '',
            riss11,
            riss12,
            riss13,
            riss14,
            riss15,
            riss16,
            riss17,
            '',
        ]

        for line in linje1_text:
            linje1.textLine(line)

        linje2 = c.beginText()
        linje2.setTextOrigin(62.5 * mm, 20 * mm)
        linje2.setFont('Helvetica', 12)

        under_r_grense = '= ( 1.6 * r^2 + t^2 )^(1/2) - 0.675 * t'
        under_r_grense2 = f'= ( 1.6 * {round(radius, 2)}^2 + {tykkelse}^2 )^(1/2) - 0.675 * {tykkelse}'
        over_r_grense = '= r'
        over_r_grense2 = f'= {round(radius, 2)}'

        if radius < 1.724 * tykkelse:
            a_text = under_r_grense
            a_text2 = under_r_grense2
        else:
            a_text = over_r_grense
            a_text2 = over_r_grense2

        linje2_text = [
            '',
            '',
            '',
            '',
            '',
            f'{tykkelse} mm',
            f'{betong}',
            f'{armeringstype}',
            f'{rebar_size} mm',
            f'{senteravstand} mm',
            f'{gulvklasse}',
            linje1_name2,
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '= f_ck * t^2 / ( 1.32 * log ( 1.43 * l_e / a ))',
            f'= {f_ck} * {tykkelse}^2 / ( 1.32 * log ( 1.43 * {round(l_e, 2)} / {round(a, 2)} ))',
            '',
            '= f_ck * t^2 / ( 2.34 * log ( 1.23 * l_e / a ))',
            f'= {f_ck} * {tykkelse}^2 / ( 2.34 * log ( 1.23 * {round(l_e, 2)} / {round(a, 2)} ))',
            '',
            '= f_ck * t^2 / ( 3 * ( 1 - 1.23 * ( a / l_e )^0.6 ))',
            f'= {f_ck} * {tykkelse}^2 / ( 3 * ( 1 - 1.23 * ',
            f'   ( {round(a, 2)} / {round(l_e, 2)} )^0.6 ))',
            '',
            f'{a_text}',
            f'{a_text2}',
            '',
            '= ( D  / k )^(1/4)',
            f'= ( {"{:.3e}".format(stor_d)} / {grunnstivhet} )^(1/4)',
            '',
            '= E_cm * t^3 / ( 12 * ( 1 - v^2 ))',
            f'= {e_cm} * {tykkelse}^3 / ( 12 * ( 1 - 0.2^2 ))',
            '',
            '',
            '',
            riss21,
            riss22,
            riss23,
            riss24,
            riss25,
            riss26,
            riss27,
            riss28,
            '',
            '',
        ]

        for line in linje2_text:
            linje2.textLine(line)

        linje3 = c.beginText()
        linje3.setTextOrigin(115 * mm, 20 * mm)
        linje3.setFont('Helvetica', 12)

        linje3_text = [
            '',
            '',
            '',
            '',
            '',
            'Karakteristisk last:',
            'Lastens plassering:',
            'Grunnstivhet:',
            'Lastflatens radius:',
            'Reduksjonsfaktor, b:',
            'Overdekning:',
            'x:',
            'y:',
        ]

        for line in linje3_text:
            linje3.textLine(line)

        linje4 = c.beginText()
        linje4.setTextOrigin(157.5 * mm, 20 * mm)
        linje4.setFont('Helvetica', 12)

        linje4_text = [
            '',
            '',
            '',
            '',
            '',
            f'{round(last / 1000, 2)} kN',
            f'{lastplassering}',
            f'{round(grunnstivhet, 4)}',
            f'{round(radius, 2)} mm',
            f'{reduksjonsfaktor}',
            f'{overdekning} mm',
            f'{x} mm',
            f'{y} mm',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            f'= {round(westergaard_senter / 1000, 2)} kN',
            '',
            '',
            f'= {round(westergaard_kant / 1000, 2)} kN',
            '',
            '',
            '',
            f'= {round(westergaard_hjorne / 1000, 2)} kN',
            '',
            '',
            f'= {round(a, 2)} mm',
            '',
            '',
            f'= {round(l_e, 2)} mm',
            '',
            '',
            f'= {"{:.3e}".format(stor_d)} Nmm',
            '',
            '',
            '',
            '',
            riss31,
            riss32,
            riss33,
            riss34,
            riss35,
            riss36,
            riss37,
            '',
            '',
        ]

        for line in linje4_text:
            linje4.textLine(line)

        c.drawText(linje1)
        c.drawText(linje2)
        c.drawText(linje3)
        c.drawText(linje4)
        c.showPage()

        linje5 = c.beginText()
        linje5.setTextOrigin(20 * mm, 20 * mm)
        linje5.setFont('Helvetica', 12)

        linje5_text = [
            'Kontroll i bruddgrensetilstand:',
            '',
            'Momentkapasitet, Meyerhof:',
            '',
            'P_max,senter',
            '',
            '',
            '',
            'P_max,kant',
            '',
            '',
            '',
            'P_max, hjørne',
            '',
            '',
            'M_n',
            '',
            '',
            'M_p',
            '',
            '',
            'Rho',
            '',
            '',
            'z',
            '',
            '',
            'A_s',
            '',
            '',
            '',
            'Kapasitet ved topunkts- og firepunkts lasttilfelle:',
            '',
            'P_max,dual',
            '',
            '',
            '',
            'P_max,quad',
            '',
        ]

        for line in linje5_text:
            linje5.textLine(line)

        linje6 = c.beginText()
        linje6.setTextOrigin(62.5 * mm, 20 * mm)
        linje6.setFont('Helvetica', 12)

        if a / l_e < 0.2:
            dual = '= ( 2pi + 1.8 * x / l_e ) * ( M_p + M_n )'
            dual2 = f'= ( 2pi + 1.8 * {x} / {round(l_e, 2)} ) * ( {"{:.3e}".format(m_p)} + {"{:.3e}".format(m_n)} )'
            quad = '= ( 2pi + 1.8 * ( x + y ) / l_e ) * ( M_p + M_n )'
            quad2 = f'= ( 2pi + 1.8 * ( {x} + {y} ) / {round(l_e, 2)} ) * ( {"{:.3e}".format(m_p)} + {"{:.3e}".format(m_n)} )'
            dual21 = ''
            quad21 = ''
        else:
            dual = '= ( 4pi / ( 1 - a / 3 * l_e ) + 1.8 * x / ( 1 - a / 2 )) * ( M_p + M_n )'
            dual2 = f'= ( 4pi / ( 1 - {round(a, 2)} / 3 * {round(l_e, 2)} ) + 1.8 * {x} /'
            dual21 = f'   ( 1 - {round(a, 2)} / 2 )) * ( {"{:.3e}".format(m_p)} + {"{:.3e}".format(m_n)} )'
            quad = '= ( 4pi / ( 1 - a / 3 * l_e ) + 1.8 * ( x + y ) / ( 1 - a / 2 )) * ( M_p + M_n )'
            quad2 = f'= ( 4pi / ( 1 - {round(a, 2)} / 3 * {round(l_e, 2)} ) + 1.8 * ( {x} + {y} ) / '
            quad21 = f'   ( 1 - {round(a, 2)} / 2 )) * ( {"{:.3e}".format(m_p)} + {"{:.3e}".format(m_n)} )'

        if armeringstype == 'slakkarmering enkel' or armeringstype == 'nettarmering enkel':
            linje6_as = '= pi * ( Ø / 2 )^2 * 1000 / cc'
            linje6_as2 = f'= 3.142 * ( {rebar_size} / 2 )^2 * 1000 / {senteravstand}'
        elif armeringstype == 'slakkarmering dobbel' or armeringstype == 'nettarmering dobbel':
            linje6_as = '= pi * ( Ø / 2 )^2 * 1000 / cc * 2'
            linje6_as2 = f'= 3.142 * ( {rebar_size} / 2 )^2 * 1000 / {senteravstand} * 2'
        else:
            linje6_as = ''
            linje6_as2 = ''

        if armeringstype == 'slakkarmering enkel' or armeringstype == 'nettarmering enkel':
            linje6_mn = '= f_sd * A_s * z'
            linje6_mn2 = f'= {round(500 / 1.15, 2)} * {round(a_s, 2)} * {z}'
        elif armeringstype == 'slakkarmering dobbel' or armeringstype == 'nettarmering dobbel':
            linje6_mn = '= f_sd * A_s / 2 * z'
            linje6_mn2 = f'= {round(500 / 1.15, 2)} * {round(a_s, 2)} / 2 * {z}'
        else:
            linje6_mn = ''
            linje6_mn2 = ''

        if armeringstype == 'slakkarmering enkel' or armeringstype == 'nettarmering enkel':
            linje6_mp = '= f_ctd * ( t^2 / 6 )'
            linje6_mp2 = f'= {round(f_ctd, 3)} * ( {tykkelse}^2 / 6 )'
            linje7_mp = f'= {"{:.3e}".format(m_p / 1000000)} kNm'
        elif armeringstype == 'slakkarmering dobbel' or armeringstype == 'nettarmering dobbel':
            linje6_mp = '= f_sd * A_s / 2 * z'
            linje6_mp2 = f'= {round(500 / 1.15, 2)} * {round(a_s, 2)} / 2 * {z}'
            linje7_mp = f'= {round(m_p / 1000000, 2)} kNm'
        else:
            linje6_mp = ''
            linje6_mp2 = ''
            linje7_mp = ''

        linje6_text = [
            '',
            '',
            '',
            '',
            '= 6 * ( 1 + 2a / l_e ) * ( M_p + M_n )',
            f'= 6 * ( 1 + 2 * {round(a, 2)} / {round(l_e, 2)} * ',
            f'   ( {"{:.3e}".format(m_p)} + {"{:.3e}".format(m_n)} )',
            '',
            '= 3.5 * ( 1 + 3a / l_e ) * ( M_p + M_n )',
            f'= 3.5 * ( 1 + 3 * {round(a, 2)} / {round(l_e, 2)} * ',
            f'   ( {"{:.3e}".format(m_p)} + {"{:.3e}".format(m_n)} )',
            '',
            '= 2 * ( 1 + 4a / l_e ) * M_n',
            f'= 2 * ( 1 + 4 * {round(a, 2)} / {round(l_e, 2)} ) * {"{:.3e}".format(m_n)}',
            '',
            linje6_mn,
            linje6_mn2,
            '',
            linje6_mp,
            linje6_mp2,
            '',
            '= A_s / ( b * d_eff )',
            f'= {round(a_s, 2)} / ( 1000 * {d_eff}',
            '',
            '= 0.6 * t',
            f'= 0.6 * {tykkelse}',
            '',
            linje6_as,
            linje6_as2,
            '',
            '',
            '',
            '',
            f'{dual}',
            f'{dual2}',
            f'{dual21}',
            '',
            f'{quad}',
            f'{quad2}',
            f'{quad21}',
            '',
        ]

        for line in linje6_text:
            linje6.textLine(line)

        linje7 = c.beginText()
        linje7.setTextOrigin(115 * mm, 20 * mm)
        linje7.setFont('Helvetica', 12)

        linje7_text = [
            '',
        ]

        for line in linje7_text:
            linje7.textLine(line)

        linje8 = c.beginText()
        linje8.setTextOrigin(157.5 * mm, 20 * mm)
        linje8.setFont('Helvetica', 12)

        linje8_text = [
            '',
            '',
            '',
            '',
            '',
            '',
            f'= {round(meyerhof_senter / 1000, 2)} kN',
            '',
            '',
            '',
            f'= {round(meyerhof_kant / 1000, 2)} kN',
            '',
            '',
            f'= {round(meyerhof_hjorne / 1000, 2)} kN',
            '',
            '',
            f'= {round(m_n / 1000000, 2)} kNm',
            '',
            '',
            linje7_mp,
            '',
            '',
            f'= {"{:.3e}".format(rho)}',
            '',
            '',
            f'= {round(z, 2)} mm',
            '',
            '',
            f'= {round(a_s, 2)} mm^2',
            '',
            '',
            '',
            '',
            '',
            '',
            f'= {round(dual_point / 1000, 2)} kN',
            '',
            '',
            '',
            f'= {round(quadruple_point / 1000, 2)} kN',
            '',
        ]

        for line in linje8_text:
            linje8.textLine(line)

        c.drawText(linje5)
        c.drawText(linje6)
        c.drawText(linje7)
        c.drawText(linje8)
        c.showPage()

        linje9 = c.beginText()
        linje9.setTextOrigin(20 * mm, 20 * mm)
        linje9.setFont('Helvetica', 12)

        linje9_text = [
            'Skjærkapasitet:',
            '',
            'Skjærstrekk:',
            '',
            'V_Ed,1,senter',
            '',
            '',
            'V_Ed,1,kant',
            '',
            '',
            'V_Ed,1,hjørne',
            '',
            '',
            'v_Rd',
            '',
            '',
            '',
            'v_min',
            '',
            '',
            'k_ec2',
            '',
            '',
            'u_1,senter',
            '',
            '',
            'u_1,kant',
            '',
            '',
            'u_1,hjørne',
            '',
            '',
            'C_Rd,c',
            '',
            '',
            'd_eff',
            '',
        ]

        for line in linje9_text:
            linje9.textLine(line)

        linje10 = c.beginText()
        linje10.setTextOrigin(62.5 * mm, 20 * mm)
        linje10.setFont('Helvetica', 12)

        if armeringstype == 'slakkarmering enkel' or armeringstype == 'nettarmering enkel':
            d_eff_linje = '= c_nom + Ø'
            d_eff_linje2 = f'= {overdekning} + {rebar_size}'
        elif armeringstype == 'slakkarmering dobbel' or armeringstype == 'nettarmering dobbel':
            d_eff_linje = '= t - c_nom - Ø'
            d_eff_linje2 = f'= {tykkelse} - {overdekning} - {rebar_size}'
        else:
            d_eff_linje = ''
            d_eff_linje2 = ''

        linje10_text = [
            '',
            '',
            '',
            '',
            '= v_Rd * u_1,senter * d_eff',
            f'= {round(v_rd_2, 4)} * {round(u_1_senter, 2)} * {d_eff}',
            '',
            '= v_Rd * u_1,kant * d_eff',
            f'= {round(v_rd_2, 4)} * {round(u_1_kant, 2)} * {d_eff}',
            '',
            '= v_Rd * u_1,hjørne * d_eff',
            f'= {round(v_rd_2, 4)} * {round(u_1_hjorne, 2)} * {d_eff}',
            '',
            '= C_Rd,c * k_ec2 * ( 100 * rho_l * f_ck )^(1/3) >= v_min',
            f'= {c_rdc} * {round(k_ec2, 3)} * ( 100 * {"{:.3e}".format(rho)} * {f_ck} )^(1/3) ',
            f'   >= {round(v_min, 4)}',
            '',
            '= 0.035 * k^(3/2) * f_ck^(1/2)',
            f'= 0.035 * {round(k_ec2, 3)}^(3/2) * {f_ck}^(1/2)',
            '',
            '= 1 + ( 200 / d_eff )^(1/2) <= 2.0',
            f'= 1 + ( 200 / {d_eff} )^(1/2) <= 2.0',
            '',
            '= 2pi * ( r + 2 * d_eff )',
            f'= 2pi * ( {round(radius, 2)} + 2 * {d_eff} )',
            '',
            '= pi * ( r + 2 * d_eff )',
            f'= pi * ( {round(radius, 2)} + 2 * {d_eff} )',
            '',
            '= pi / 2 * ( r + 2 * d_eff )',
            f'= pi / 2 * ( {round(radius, 2)} + 2 * {d_eff} )',
            '',
            '= k_2 / gamma_c',
            '= 0.15 / 1.5',
            '',
            d_eff_linje,
            d_eff_linje2,
            '',
        ]

        for line in linje10_text:
            linje10.textLine(line)

        linje11 = c.beginText()
        linje11.setTextOrigin(115 * mm, 20 * mm)
        linje11.setFont('Helvetica', 12)

        linje11_text = [
            '',
        ]

        for line in linje11_text:
            linje11.textLine(line)

        linje12 = c.beginText()
        linje12.setTextOrigin(157.5 * mm, 20 * mm)
        linje12.setFont('Helvetica', 12)

        linje12_text = [
            '',
            '',
            '',
            '',
            '',
            f'= {round(v_ed_1_senter / 1000, 2)} kN',
            '',
            '',
            f'= {round(v_ed_1_kant / 1000, 2)} kN',
            '',
            '',
            f'= {round(v_ed_1_hjorne / 1000, 2)} kN',
            '',
            '',
            '',
            f'= {round(v_rd_2, 4)} N/mm^2',
            '',
            '',
            f'= {round(v_min, 4)} N/mm^2',
            '',
            '',
            f'= {round(k_ec2, 2)}',
            '',
            '',
            f'= {round(u_1_senter, 2)} mm',
            '',
            '',
            f'= {round(u_1_kant, 2)} mm',
            '',
            '',
            f'= {round(u_1_hjorne, 2)} mm',
            '',
            '',
            '= 0.1',
            '',
            '',
            f'= {d_eff} mm',
            '',
        ]

        for line in linje12_text:
            linje12.textLine(line)

        c.drawText(linje9)
        c.drawText(linje10)
        c.drawText(linje11)
        c.drawText(linje12)
        c.showPage()

        linje13 = c.beginText()
        linje13.setTextOrigin(20 * mm, 20 * mm)
        linje13.setFont('Helvetica', 12)

        linje13_text = [
            'Skjærkapasitet:',
            '',
            'Skjærtrykk:',
            '',
            'V_Ed,0,senter',
            '',
            '',
            'V_Ed,0,kant',
            '',
            '',
            'V_Ed,0,hjørne',
            '',
            '',
            'v_Rd,max',
            '',
            '',
            'v_2',
            '',
            '',
            'u_0,senter',
            '',
            '',
            'u_0,kant',
            '',
            '',
            'u_0,hjørne',
            '',
            '',
            '',
            '',
            'Kontroll minimumsarmering:',
            '',
            'A_s,min',
            '',
            '',
            'A_s / A_s,min',
            '',
            '',
            '',
            '',
            'Pris',
            '',
            '',
            '',
            'GWP',
            '',
        ]

        for line in linje13_text:
            linje13.textLine(line)

        linje14 = c.beginText()
        linje14.setTextOrigin(62.5 * mm, 20 * mm)
        linje14.setFont('Helvetica', 12)

        linje14_text = [
            '',
            '',
            '',
            '',
            '= v_Rd,max * u_0,senter * d_eff',
            f'= {round(v_rd_max, 4)} * {round(u_0_senter, 2)} * {d_eff}',
            '',
            '= v_Rd,max * u_0,kant * d_eff',
            f'= {round(v_rd_max, 4)} * {round(u_0_kant, 2)} * {d_eff}',
            '',
            '= v_Rd,max * u_0,hjørne * d_eff',
            f'= {round(v_rd_max, 4)} * {round(u_0_hjorne, 2)} * {d_eff}',
            '',
            '= 0.4 * v_2 * f_cd',
            f'= 0.4 * {round(v_2, 4)} * {round(f_cd, 2)}',
            '',
            '= 0.6 * ( 1 - f_ck / 250 )',
            f'= 0.6 * ( 1- {f_ck} / 250 )',
            '',
            '= 2pi * r',
            f'= 2pi * {round(radius, 2)}',
            '',
            '= pi * r',
            f'= pi * {round(radius, 2)}',
            '',
            '= pi * r / 2',
            f'= pi * {round(radius, 2)} / 2',
            '',
            '',
            '',
            '',
            '',
            '= 0.26 * f_ctm / f_yk * b * t',
            f'= 0.26 * {f_ctm} / 500 * 1000 * {tykkelse}',
            '',
            f'= {round(a_s, 2)} / {round(a_s_min, 2)}',
            '',
            '',
            '',
            '',
            '= armeringspris * armering per m^2 + ',
            '   betongpris * betong per m^2',
            f'= {round(rebar_price_input, 2)} * {round(as_per_square_meter, 2)} + {round(concrete_price_input, 2)} *'
            f' {round(concrete_per_square_meter, 2)}',
            '',
            '= armering gwp * armering per m^2 + ',
            '   betong gwp * betong per m^2',
            f'= {round(rebar_gwp_input, 2)} * {round(as_per_square_meter, 2)} + {round(concrete_gwp_input, 2)} *'
            f' {round(concrete_per_square_meter, 2)}',
            '',
        ]

        for line in linje14_text:
            linje14.textLine(line)

        linje15 = c.beginText()
        linje15.setTextOrigin(157.5 * mm, 20 * mm)
        linje15.setFont('Helvetica', 12)

        linje15_text = [
            '',
            '',
            '',
            '',
            '',
            f'= {round(v_ed_0_senter / 1000, 2)} kN',
            '',
            '',
            f'= {round(v_ed_0_kant / 1000, 2)} kN',
            '',
            '',
            f'= {round(v_ed_0_hjorne / 1000, 2)} kN',
            '',
            '',
            f'= {round(v_rd_max, 4)} N/mm^2',
            '',
            '',
            f'= {round(v_2, 4)}',
            '',
            '',
            f'= {round(u_0_senter, 2)} mm',
            '',
            '',
            f'= {round(u_0_kant, 2)} mm',
            '',
            '',
            f'= {round(u_0_hjorne, 2)} mm',
            '',
            '',
            '',
            '',
            '',
            '',
            f'= {round(a_s_min, 2)} mm^2',
            '',
            f'= {round(a_s / a_s_min, 2)}',
            '',
            '',
            '',
            '',
            '',
            '',
            f'= {round(price_sum, 2)} NOK / m^2',
            '',
            '',
            '',
            f'= {round(gwp_sum, 2)} kg C02 eq. / m^2',
            '',
        ]

        for line in linje15_text:
            linje15.textLine(line)

        c.drawText(linje13)
        c.drawText(linje14)
        c.drawText(linje15)
        c.showPage()
        c.save()
        os.startfile(tittel)
    except PermissionError:
        tkinter.messagebox.showinfo('Feilmelding', 'Vennligst lukk pdf dokumenter som er åpne!')
    except ZeroDivisionError:
        pass


# create_pdf('Slakkarmert gulv på grunn - Rapport.pdf')
