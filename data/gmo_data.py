import pandas as pd

data = {
    'gmo_name': [
        'MON 810 Maize', 'Bt11 Maize', 'GTS 40-3-2 Soybean',
        'MON 40-3-2 Soybean', 'GT73 Rapeseed', 'MON 863 Maize',
        'MON 89788 Soybean', 'DAS-44406-6 Soybean', 'DP-305423 Soybean',
        'MON 87701 Soybean', 'ACS-BNØØ4 Rapeseed', 'MON 87460 Maize',
        'FLEXmi Cotton', 'MON 531 Cotton', 'Golden Rice GR2E',
        'AquAdvantage Salmon', 'Innate Potato', 'Arctic Apple',
        'MON 87427 Maize', 'SU Canola'
    ],
    'crop_type': [
        'Maize', 'Maize', 'Soybean',
        'Soybean', 'Rapeseed', 'Maize',
        'Soybean', 'Soybean', 'Soybean',
        'Soybean', 'Rapeseed', 'Maize',
        'Cotton', 'Cotton', 'Rice',
        'Animal', 'Potato', 'Apple',
        'Maize', 'Rapeseed'
    ],
    'use_category': [
        'Agricultural', 'Agricultural', 'Agricultural',
        'Agricultural', 'Agricultural', 'Agricultural',
        'Agricultural', 'Agricultural', 'Agricultural',
        'Agricultural', 'Agricultural', 'Agricultural',
        'Agricultural', 'Agricultural', 'Medical',
        'Food', 'Food', 'Food',
        'Agricultural', 'Agricultural'
    ],
    'approval_status': [
        'Approved', 'Approved', 'Approved',
        'Approved', 'Approved', 'Approved',
        'Approved', 'Approved', 'Approved',
        'Approved', 'Approved', 'Approved',
        'Pending', 'Approved', 'Approved',
        'Approved', 'Approved', 'Approved',
        'Pending', 'Approved'
    ],
    'approval_year': [
        1998, 1998, 1996,
        1997, 1997, 2003,
        2007, 2012, 2009,
        2010, 2002, 2011,
        2020, 1995, 2021,
        2015, 2014, 2015,
        2019, 2000
    ],
    'risk_score': [
        2.1, 2.3, 1.8,
        1.9, 2.0, 2.4,
        1.7, 2.2, 1.9,
        2.0, 2.1, 2.3,
        1.5, 1.8, 2.6,
        3.1, 1.4, 1.3,
        2.0, 1.9
    ],
    'approved_regions': [
        'EU, USA, Canada', 'EU, USA', 'USA, Canada, EU',
        'USA, Brazil', 'EU, Canada', 'USA, Canada',
        'USA, Brazil, Argentina', 'USA, Canada', 'USA',
        'USA, Brazil', 'EU', 'USA, Canada',
        'USA', 'USA, EU, Brazil', 'Philippines',
        'USA, Canada', 'USA', 'USA, Canada',
        'USA', 'Canada, Australia'
    ]
}

df = pd.DataFrame(data)
df.to_csv('gmo_dataset.csv', index=False)
print(f"Dataset yaradıldı! {len(df)} məhsul.")
print(df['crop_type'].value_counts())