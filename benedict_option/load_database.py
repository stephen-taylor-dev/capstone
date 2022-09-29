from benedict_option.models import Liturgy, User, Group, Group_Invite



A = Liturgy.objects.create(
    author='David',
    text='1 Blessed is the man that walketh not in the counsel of the ungodly, nor standeth in the way of sinners, nor sitteth in the seat of the scornful.\n\n2 But his delight is in the law of the Lord; and in his law doth he meditate day and night\n\n3 And he shall be like a tree planted by the rivers of water, that bringeth forth his fruit in his season; his leaf also shall not wither; and whatsoever he doeth shall prosper.\n\n4 The ungodly are not so: but are like the chaff which the wind driveth away.\n\n5 Therefore the ungodly shall not stand in the judgment, nor sinners in the congregation of the righteous.\n\n6 For the Lord knoweth the way of the righteous: but the way of the ungodly shall perish.',
    title='Psalm 1',
    type='Psalm',
    length= 3
)

B = Liturgy.objects.create(
    author='David',
    text="1 Why do the heathen rage, and the people imagine a vain thing?\n\n2 The kings of the earth set themselves, and the rulers take counsel together, against the Lord, and against his anointed, saying,\n\n3 Let us break their bands asunder, and cast away their cords from us.\n\n4 He that sitteth in the heavens shall laugh: the Lord shall have them in derision.\n\n5 Then shall he speak unto them in his wrath, and vex them in his sore displeasure.\n\n6 Yet have I set my king upon my holy hill of Zion.\n\n7 I will declare the decree: the Lord hath said unto me, Thou art my Son; this day have I begotten thee.\n\n8 Ask of me, and I shall give thee the heathen for thine inheritance, and the uttermost parts of the earth for thy possession.\n\n9 Thou shalt break them with a rod of iron; thou shalt dash them in pieces like a potter's vessel.\n\n10 Be wise now therefore, O ye kings: be instructed, ye judges of the earth.\n\n11 Serve the Lord with fear, and rejoice with trembling.\n\n12 Kiss the Son, lest he be angry, and ye perish from the way, when his wrath is kindled but a little. Blessed are all they that put their trust in him.",
    title='Psalm 2',
    type='Psalm',
    length= 3
)

C = Liturgy.objects.create(
    author='David',
    text="1 Lord, how are they increased that trouble me! many are they that rise up against me.\n\n2 Many there be which say of my soul, There is no help for him in God. Selah.\n\n3 But thou, O Lord, art a shield for me; my glory, and the lifter up of mine head.\n\n4 I cried unto the Lord with my voice, and he heard me out of his holy hill. Selah.\n\n5 I laid me down and slept; I awaked; for the Lord sustained me.\n\n6 I will not be afraid of ten thousands of people, that have set themselves against me round about.\n\n7 Arise, O Lord; save me, O my God: for thou hast smitten all mine enemies upon the cheek bone; thou hast broken the teeth of the ungodly.\n\n8 Salvation belongeth unto the Lord: thy blessing is upon thy people. Selah.",
    title='Psalm 3',
    type='Psalm',
    length= 1
)

D = Liturgy.objects.create(
    author='David',
    text="1 Hear me when I call, O God of my righteousness: thou hast enlarged me when I was in distress; have mercy upon me, and hear my prayer.\n\n2 O ye sons of men, how long will ye turn my glory into shame? how long will ye love vanity, and seek after leasing? Selah.\n\n3 But know that the Lord hath set apart him that is godly for himself: the Lord will hear when I call unto him.\n\n4 Stand in awe, and sin not: commune with your own heart upon your bed, and be still. Selah.\n\n5 Offer the sacrifices of righteousness, and put your trust in the Lord.\n\n6 There be many that say, Who will shew us any good? Lord, lift thou up the light of thy countenance upon us.\n\n7 Thou hast put gladness in my heart, more than in the time that their corn and their wine increased.\n\n8 I will both lay me down in peace, and sleep: for thou, Lord, only makest me dwell in safety.",
    title='Psalm 4',
    type='Psalm',
    length= 1
)

E = Liturgy.objects.create(
    author='David',
    text="1 Give ear to my words, O Lord, consider my meditation.\n\n2 Hearken unto the voice of my cry, my King, and my God: for unto thee will I pray.\n\n3 My voice shalt thou hear in the morning, O Lord; in the morning will I direct my prayer unto thee, and will look up.\n\n4 For thou art not a God that hath pleasure in wickedness: neither shall evil dwell with thee.\n\n5 The foolish shall not stand in thy sight: thou hatest all workers of iniquity.\n\n6 Thou shalt destroy them that speak leasing: the Lord will abhor the bloody and deceitful man.\n\n7 But as for me, I will come into thy house in the multitude of thy mercy: and in thy fear will I worship toward thy holy temple.\n\n8 Lead me, O Lord, in thy righteousness because of mine enemies; make thy way straight before my face.\n\n9 For there is no faithfulness in their mouth; their inward part is very wickedness; their throat is an open sepulchre; they flatter with their tongue.\n\n10 Destroy thou them, O God; let them fall by their own counsels; cast them out in the multitude of their transgressions; for they have rebelled against thee.\n\n11 But let all those that put their trust in thee rejoice: let them ever shout for joy, because thou defendest them: let them also that love thy name be joyful in thee.\n\n12 For thou, Lord, wilt bless the righteous; with favour wilt thou compass him as with a shield.",
    title='Psalm 5',
    type='Psalm',
    length= 2
)

F = Liturgy.objects.create(
    author='David',
    text="1 O Lord, rebuke me not in thine anger, neither chasten me in thy hot displeasure.\n\n2 Have mercy upon me, O Lord; for I am weak: O Lord, heal me; for my bones are vexed.\n\n3 My soul is also sore vexed: but thou, O Lord, how long?\n\n4 Return, O Lord, deliver my soul: oh save me for thy mercies' sake.\n\n5 For in death there is no remembrance of thee: in the grave who shall give thee thanks?\n\n6 I am weary with my groaning; all the night make I my bed to swim; I water my couch with my tears.\n\n7 Mine eye is consumed because of grief; it waxeth old because of all mine enemies.\n\n8 Depart from me, all ye workers of iniquity; for the Lord hath heard the voice of my weeping.\n\n9 The Lord hath heard my supplication; the Lord will receive my prayer.\n\n10 Let all mine enemies be ashamed and sore vexed: let them return and be ashamed suddenly.",
    title='Psalm 6',
    type='Psalm',
    length= 2
)


G = Liturgy.objects.create(
    author='David',
    text="1 O Lord my God, in thee do I put my trust: save me from all them that persecute me, and deliver me:\n\n2 Lest he tear my soul like a lion, rending it in pieces, while there is none to deliver.\n\n3 O Lord my God, If I have done this; if there be iniquity in my hands;\n\n4 If I have rewarded evil unto him that was at peace with me; (yea, I have delivered him that without cause is mine enemy:)\n\n5 Let the enemy persecute my soul, and take it; yea, let him tread down my life upon the earth, and lay mine honour in the dust. Selah.\n\n6 Arise, O Lord, in thine anger, lift up thyself because of the rage of mine enemies: and awake for me to the judgment that thou hast commanded.\n\n7 So shall the congregation of the people compass thee about: for their sakes therefore return thou on high.\n\n8 The Lord shall judge the people: judge me, O Lord, according to my righteousness, and according to mine integrity that is in me.\n\n9 Oh let the wickedness of the wicked come to an end; but establish the just: for the righteous God trieth the hearts and reins.\n\n10 My defence is of God, which saveth the upright in heart.\n\n11 God judgeth the righteous, and God is angry with the wicked every day.\n\n12 If he turn not, he will whet his sword; he hath bent his bow, and made it ready.\n\n13 He hath also prepared for him the instruments of death; he ordaineth his arrows against the persecutors.\n\n14 Behold, he travaileth with iniquity, and hath conceived mischief, and brought forth falsehood.\n\n15 He made a pit, and digged it, and is fallen into the ditch which he made.\n\n16 His mischief shall return upon his own head, and his violent dealing shall come down upon his own pate.\n\n17 I will praise the Lord according to his righteousness: and will sing praise to the name of the Lord most high.",
    title='Psalm 7',
    type='Psalm',
    length= 4
)


H = Liturgy.objects.create(
    author='David',
    text="1 O Lord, our Lord, how excellent is thy name in all the earth! who hast set thy glory above the heavens.\n\n2 Out of the mouth of babes and sucklings hast thou ordained strength because of thine enemies, that thou mightest still the enemy and the avenger.\n\n3 When I consider thy heavens, the work of thy fingers, the moon and the stars, which thou hast ordained;\n\n4 What is man, that thou art mindful of him? and the son of man, that thou visitest him?\n\n5 For thou hast made him a little lower than the angels, and hast crowned him with glory and honour.\n\n6 Thou madest him to have dominion over the works of thy hands; thou hast put all things under his feet:\n\n7 All sheep and oxen, yea, and the beasts of the field;\n\n8 The fowl of the air, and the fish of the sea, and whatsoever passeth through the paths of the seas.\n\n9 O Lord our Lord, how excellent is thy name in all the earth!",
    title='Psalm 8',
    type='Psalm',
    length= 1
)

I = Liturgy.objects.create(
    author='David',
    text="1 I will praise thee, O Lord, with my whole heart; I will shew forth all thy marvellous works.\n\n2 I will be glad and rejoice in thee: I will sing praise to thy name, O thou most High.\n\n3 When mine enemies are turned back, they shall fall and perish at thy presence.\n\n4 For thou hast maintained my right and my cause; thou satest in the throne judging right.\n\n5 Thou hast rebuked the heathen, thou hast destroyed the wicked, thou hast put out their name for ever and ever.\n\n6 O thou enemy, destructions are come to a perpetual end: and thou hast destroyed cities; their memorial is perished with them.\n\n7 But the Lord shall endure for ever: he hath prepared his throne for judgment.\n\n8 And he shall judge the world in righteousness, he shall minister judgment to the people in uprightness.\n\n9 The Lord also will be a refuge for the oppressed, a refuge in times of trouble.\n\n10 And they that know thy name will put their trust in thee: for thou, Lord, hast not forsaken them that seek thee.\n\n11 Sing praises to the Lord, which dwelleth in Zion: declare among the people his doings.\n\n12 When he maketh inquisition for blood, he remembereth them: he forgetteth not the cry of the humble.\n\n13 Have mercy upon me, O Lord; consider my trouble which I suffer of them that hate me, thou that liftest me up from the gates of death:\n\n14 That I may shew forth all thy praise in the gates of the daughter of Zion: I will rejoice in thy salvation.\n\n15 The heathen are sunk down in the pit that they made: in the net which they hid is their own foot taken.\n\n16 The Lord is known by the judgment which he executeth: the wicked is snared in the work of his own hands. Higgaion. Selah.\n\n17 The wicked shall be turned into hell, and all the nations that forget God.\n\n18 For the needy shall not always be forgotten: the expectation of the poor shall not perish for ever.\n\n19 Arise, O Lord; let not man prevail: let the heathen be judged in thy sight.\n\n20 Put them in fear, O Lord: that the nations may know themselves to be but men. Selah.",
    title='Psalm 9',
    type='Psalm',
    length= 10
)

J = Liturgy.objects.create(
    author='David',
    text="1 Why standest thou afar off, O Lord? why hidest thou thyself in times of trouble?\n\n2 The wicked in his pride doth persecute the poor: let them be taken in the devices that they have imagined.\n\n3 For the wicked boasteth of his heart's desire, and blesseth the covetous, whom the Lord abhorreth.\n\n4 The wicked, through the pride of his countenance, will not seek after God: God is not in all his thoughts.\n\n5 His ways are always grievous; thy judgments are far above out of his sight: as for all his enemies, he puffeth at them.\n\n6 He hath said in his heart, I shall not be moved: for I shall never be in adversity.\n\n7 His mouth is full of cursing and deceit and fraud: under his tongue is mischief and vanity.\n\n8 He sitteth in the lurking places of the villages: in the secret places doth he murder the innocent: his eyes are privily set against the poor.\n\n9 He lieth in wait secretly as a lion in his den: he lieth in wait to catch the poor: he doth catch the poor, when he draweth him into his net.\n\n10 He croucheth, and humbleth himself, that the poor may fall by his strong ones.\n\n11 He hath said in his heart, God hath forgotten: he hideth his face; he will never see it.\n\n12 Arise, O Lord; O God, lift up thine hand: forget not the humble.\n\n13 Wherefore doth the wicked contemn God? he hath said in his heart, Thou wilt not require it.\n\n14 Thou hast seen it; for thou beholdest mischief and spite, to requite it with thy hand: the poor committeth himself unto thee; thou art the helper of the fatherless.\n\n15 Break thou the arm of the wicked and the evil man: seek out his wickedness till thou find none.\n\n16 The Lord is King for ever and ever: the heathen are perished out of his land.\n\n17 Lord, thou hast heard the desire of the humble: thou wilt prepare their heart, thou wilt cause thine ear to hear:\n\n18 To judge the fatherless and the oppressed, that the man of the earth may no more oppress.",
    title='Psalm 10',
    type='Psalm',
    length= 10
)


A.save()
B.save()
C.save()
D.save()
E.save()
F.save()
G.save()
H.save()
I.save()
J.save()


item = Group.objects.create(
    name="Public"

)

