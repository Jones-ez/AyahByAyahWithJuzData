import json

def ayahObject(juz, surah, ayah, arabic):
    return {
        'juz': juz,
        'surah': surah,
        'ayah': ayah,
        'arabic': arabic
    }

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

for surah in range(1, 115):
    with open(f"data/surah/surah_"+str(surah)+".json") as surahData:
        surahData = json.load(surahData)
        ayahNumber = surahData['count']
        juzs = surahData['juz']
        ayahs = []

        for juz in juzs:
            start = int(juz['verse']['start'].replace('verse_', ''))
            end = int(juz['verse']['end'].replace('verse_', ''))
            for ayah in range(1, (ayahNumber+1)):
                if((ayah>=start)&(ayah<=end)):
                    ayahs.append(
                        ayahObject(
                            int(juz['index']),
                            surah,
                            ayah,
                            (surahData['verse']['verse_'+str(ayah)])
                        )
                    )       

        with open(f'data/ayahs/arabicBySurahWithJuzData/surah_'+str(surah)+'.json', 'w', encoding="utf-8") as surahFile:
            json.dump(ayahs, surahFile, default=set_default, ensure_ascii=False, indent=3)
            print('surah_'+str(surah)+'.json saved')
            
