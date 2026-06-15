import pandas as pd

# GMO Safety Dataset - manually curated from EFSA, USDA, WHO sources
data = {
    'gmo_name': [
        'MON 810 Maize', 'Bt11 Maize', 'GTS 40-3-2 Soybean',
        'MON 40-3-2 Soybean', 'GT73 Rapeseed', 'MON 863 Maize',
        'MON 89788 Soybean', 'DAS-44406-6 Soybean', 'DP-305423 Soybean',
        'MON 87701 Soybean'
    ],
    'crop_type': [
        'Maize', 'Maize', 'Soybean',
        'Soybean', 'Rapeseed', 'Maize',
        'Soybean', 'Soybean', 'Soybean',
        'Soybean'
    ],
    'use_category': [
        'Agricultural', 'Agricultural', 'Agricultural',
        'Agricultural', 'Agricultural', 'Agricultural',
        'Agricultural', 'Agricultural', 'Agricultural',
        'Agricultural'
    ],
    'approval_status': [
        'Approved', 'Approved', 'Approved',
        'Approved', 'Approved', 'Approved',
        'Approved', 'Approved', 'Approved',
        'Approved'
    ],
    'approval_year': [
        1998, 1998, 1996,
        1997, 1997, 2003,
        2007, 2012, 2009,
        2010
    ],
    'risk_score': [
        2.1, 2.3, 1.8,
        1.9, 2.0, 2.4,
        1.7, 2.2, 1.9,
        2.0
    ],
    'approved_regions': [
        'EU, USA, Canada', 'EU, USA', 'USA, Canada, EU',
        'USA, Brazil', 'EU, Canada', 'USA, Canada',
        'USA, Brazil, Argentina', 'USA, Canada', 'USA',
        'USA, Brazil'
    ]
}

df = pd.DataFrame(data)
df.to_csv('gmo_dataset.csv', index=False)
print("Dataset yaradıldı!")
print(df.head())