from benedict_option.models import Liturgy, User, Group, Group_Invite



A = Liturgy.objects.create(
    author='David',
    text='1 Blessed is the man that walketh not in the counsel of the ungodly, nor standeth in the way of sinners, nor sitteth in the seat of the scornful. 2 But his delight is in the law of the Lord; and in his law doth he meditate day and night. 3 And he shall be like a tree planted by the rivers of water, that bringeth forth his fruit in his season; his leaf also shall not wither; and whatsoever he doeth shall prosper. 4 The ungodly are not so: but are like the chaff which the wind driveth away. 5 Therefore the ungodly shall not stand in the judgment, nor sinners in the congregation of the righteous. 6 For the Lord knoweth the way of the righteous: but the way of the ungodly shall perish.',
    title='Psalm 1',
    type='Psalm',
    length= 3
)

B = Liturgy.objects.create(
    author='David',
    text="1 Why do the heathen rage, and the people imagine a vain thing?\r\n2 The kings of the earth set themselves, and the rulers take counsel together, against the Lord, and against his anointed, saying,\r\n3 Let us break their bands asunder, and cast away their cords from us.\r\n4 He that sitteth in the heavens shall laugh: the Lord shall have them in derision.\r\n5 Then shall he speak unto them in his wrath, and vex them in his sore displeasure.\r\n6 Yet have I set my king upon my holy hill of Zion.\r\n7 I will declare the decree: the Lord hath said unto me, Thou art my Son; this day have I begotten thee.\r\n8 Ask of me, and I shall give thee the heathen for thine inheritance, and the uttermost parts of the earth for thy possession.\r\n9 Thou shalt break them with a rod of iron; thou shalt dash them in pieces like a potter's vessel.\r\n10 Be wise now therefore, O ye kings: be instructed, ye judges of the earth.\r\n11 Serve the Lord with fear, and rejoice with trembling.\r\n12 Kiss the Son, lest he be angry, and ye perish from the way, when his wrath is kindled but a little. Blessed are all they that put their trust in him.",
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
    text="1 Lord, how are they increased that trouble me! many are they that rise up against me.\n\n2 Many there be which say of my soul, There is no help for him in God. Selah.\n\n3 But thou, O Lord, art a shield for me; my glory, and the lifter up of mine head.\n\n4 I cried unto the Lord with my voice, and he heard me out of his holy hill. Selah.\n\n5 I laid me down and slept; I awaked; for the Lord sustained me.\n\n6 I will not be afraid of ten thousands of people, that have set themselves against me round about.\n\n7 Arise, O Lord; save me, O my God: for thou hast smitten all mine enemies upon the cheek bone; thou hast broken the teeth of the ungodly.\n\n8 Salvation belongeth unto the Lord: thy blessing is upon thy people. Selah.",
    title='Psalm 4',
    type='Psalm',
    length= 1
)
L.save()

