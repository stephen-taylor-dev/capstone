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

A.save()
B.save()
C.save()
D.save()
E.save()

item = Group.objects.create(
    name="Public"

)

psalms = [A, B, C, D, E]
for psalm in psalms:
    psalm.save()

Group.objects.create(
    name='Church',
)

password = 'password'

a = User.objects.create_user(
    username='john',
    email='john@email.com',
    password=password,
)