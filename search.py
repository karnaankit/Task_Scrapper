data = ['Talent she for lively eat led sister', ' Entrance strongly packages she out rendered get quitting denoting led', ' Dwelling confined improved it he no doubtful raptures', ' Several carried through an of up attempt gravity', ' Situation to be at offending elsewhere distrusts if', ' Particular use for considered projection cultivated', ' Worth of do doubt shall it their', ' Extensive existence up me contained he pronounce do', ' Excellence inquietude assistance precaution any impression man sufficient', ' In entirely be to at settling felicity', ' Fruit two match men you seven share', ' Needed as or is enough points', ' Miles at smart \ufeffno marry whole linen mr', ' Income joy nor can wisdom summer', ' Extremely depending he gentleman improving intention rapturous as', ' Not him old music think his found enjoy merry', ' Listening acuteness dependent at or an', ' Apartments thoroughly unsatiable terminated sex how themselves', ' She are ten hours wrong walls stand early', ' Domestic perceive on an ladyship extended received do', ' Why jennings our whatever his learning gay perceive', ' Is against no he without subject', 'Bed connection unreserved preference partiality not unaffected', 'Years merit trees so think in hoped we as', 'Abilities or he perfectly pretended so strangers be exquisite', ' Oh to another chamber pleased imagine do in', ' Went me rank at last loud shot an draw', ' Excellent so to no sincerity smallness', ' Removal request delight if on he we', ' Unaffected in we by apartments astonished to decisively themselves', ' Offended ten old consider speaking', 'Up unpacked friendly ecstatic so possible humoured do', ' Ample end might folly quiet one set spoke her', ' We no am former valley assure', ' Four need spot ye said we find mile', ' Are commanded him convinced dashwoods did estimable forfeited', ' Shy celebrated met sentiments she reasonably but', ' Proposal its disposed eat advanced marriage sociable', ' Drawings led greatest add subjects endeavor gay remember', ' Principles one yet assistance you met impossible', 'Savings her pleased are several started females met', ' Short her not among being any', ' Thing of judge fruit charm views do', ' Miles mr an forty along as he', ' She education get middleton day agreement performed preserved unwilling', ' Do however as pleased offence outward beloved by present', ' By outward neither he so covered amiable greater', ' Juvenile proposal betrayed he an informed weddings followed', ' Precaution day see imprudence sympathize principles', ' At full leaf give quit to in they up', 'Do am he horrible distance marriage so although', ' Afraid assure square so happen mr an before', ' His many same been well can high that', ' Forfeited did law eagerness allowance improving assurance bed', ' Had saw put seven joy short first', ' Pronounce so enjoyment my resembled in forfeited sportsman', ' Which vexed did began son abode short may', ' Interested astonished he at cultivated or me', ' Nor brought one invited she produce her', 'Picture removal detract earnest is by', ' Esteems met joy attempt way clothes yet demesne tedious', ' Replying an marianne do it an entrance advanced', ' Two dare say play when hold', ' Required bringing me material stanhill jointure is as he', ' Mutual indeed yet her living result matter him bed whence', 'Announcing of invitation principles in', ' Cold in late or deal', ' Terminated resolution no am frequently collecting insensible he do appearance', ' Projection invitation affronting admiration if no on or', ' It as instrument boisterous frequently apartments an in', ' Mr excellence inquietude conviction is in unreserved particular', ' You fully seems stand nay own point walls', ' Increasing travelling own simplicity you astonished expression boisterous', ' Possession themselves sentiments apartments devonshire we of do discretion', ' Enjoyment discourse ye continued pronounce we necessary abilities', 'He share of first to worse', ' Weddings and any opinions suitable smallest nay', ' My he houses or months settle remove ladies appear', ' Engrossed suffering supposing he recommend do eagerness', ' Commanded no of depending extremity recommend attention tolerably', ' Bringing him smallest met few now returned surprise learning jennings', ' Objection delivered eagerness he exquisite at do in', ' Warmly up he nearer mr merely me', '']
search_term = str(input("Word to search for: "))


def build_dict(data_list):
    new_dict = {}
    index = 0
    for line in data:
        new_list = line.split()
        for item in new_list:
            if item in new_dict:
                new_dict[item].append(index)
            else:
                new_dict[item] = list()
                new_dict[item].append(index)
        index += 1
    return new_dict


search_index = build_dict(data)


def search(word, index_dict):
    if word in index_dict:
        for index in index_dict[word]:
            print(data[index])


search(search_term, search_index)
