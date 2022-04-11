from PIL import Image

photos = [
    'albert-dehon-yejC65pltJc-unsplash',
    'annie-spratt-MmW8QX5Bp0c-unsplash',
    'anton-maksimov-5642-su-3jDZM3rgpz8-unsplash',
    'ardy-arjun-WfJ9rZBdWY8-unsplash',
    'batuhan-dogan-RPHnmOqWxaY-unsplash',
    'brittany-bendabout-iZX7yO1RTsE-unsplash',
    'claudio-schwarz-lLqkzbMiPI-unsplash',
    'claudio-schwarz-4bMmpwPzCIs-unsplash',
    'claudio-schwarz-6iowSYmaFyo-unsplash',
    'claudio-schwarz-8Syjmg44nFQ-unsplash',
    'claudio-schwarz-CNuUu7F05Ao-unsplash',
    'claudio-schwarz-EGfsYbZYd6Q-unsplash',
    'claudio-schwarz-eh1DXCvFcds-unsplash',
    'claudio-schwarz-F7g4gho79ds-unsplash',
    'claudio-schwarz-Fa3Me1XTozo-unsplash',
    'claudio-schwarz-IA9ywYR8ibw-unsplash',
    'claudio-schwarz-J8njRHe3ay4-unsplash',
    'claudio-schwarz-KAhK2qi0D1w-unsplash',
    'claudio-schwarz-M23NYjYgw94-unsplash',
    'claudio-schwarz-MGrIQvbxWws-unsplash',
    'claudio-schwarz-Nc4hmYD7L7E-unsplash',
    'claudio-schwarz-NtU1zWPHfvw-unsplash',
    'claudio-schwarz-PEwWaaPNxjM-unsplash',
    'claudio-schwarz-ptnzhzAz3bM-unsplash',
    'claudio-schwarz-UKqP_6nZW1Q-unsplash',
    'claudio-schwarz-V3n3U2R25M0-unsplash',
    'claudio-schwarz-W7M6dlO7M_Y-unsplash',
    'claudio-schwarz-WSaPvtvsjCc-unsplash',
    'claudio-schwarz-ZMwQIlG8Ito-unsplash',
    'gabriella-clare-marino-aNmGQmIQRpc-unsplash',
    'gabriella-clare-marino-bB3auZ9wgug-unsplash',
    'gabriella-clare-marino-eEPrua1EXfA-unsplash',
    'gabriella-clare-marino-KG5S6fM3z_s-unsplash',
    'gabriella-clare-marino-Mguuyn1TJIQ-unsplash',
    'gabriella-clare-marino-SgNlTddwbys-unsplash',
    'gabriella-clare-marino-z2FGLCb5amo-unsplash',
    'halil-ibrahim-cetinkaya-l661E7tRKAU-unsplash',
    'maksym-tymchyk-4RRvDen6rk4-unsplash',
    'maksym-tymchyk-AAsuvkUFbzQ-unsplash',
    'marc-kleen-MqQ6dpk7qfw-unsplash',
    'micheile-com-B2oQudJevQY-unsplash',
    'micheile-com-doeWwiscUPI-unsplash',
    'mihajlo-sebalj-r_am9KeM0jU-unsplash',
    'mitchell-luo-RJtd3FSXj4A-unsplash',
    'sir-manuel-fT_lkiuxWBk-unsplash',
    'sir-manuel-sP_LGDp2HZI-unsplash',
    'the-blowup-HMyoLmScAyw-unsplash',
    'the-blowup-jfLejc0rAKI-unsplash',
    'the-blowup-oHCwlngw18w-unsplash',
    'vander-films-byYV6s752Zk-unsplash'
]

for photo in photos:
    image = Image.open('./images/' + photo + '.jpg')
    heightWidthRatio = image.size[0] / image.size[1]

    image3x = image.resize((1920, round(1920 / heightWidthRatio)))
    image2x = image.resize((round(1920 * 0.5), round(1920 * 0.5 / heightWidthRatio)))
    image1x = image.resize((round(1920 * 0.25), round(1920 * 0.25 / heightWidthRatio)))

    image3x.save('./resizedImages/' + photo + '_3x.jpg')
    image2x.save('./resizedImages/' + photo + '_2x.jpg')
    image1x.save('./resizedImages/' + photo + '_1x.jpg')

print("done")