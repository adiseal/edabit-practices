def test_fairness(agatha, bertha):
    agatha_area = sum([l * w for l, w in agatha])
    bertha_area = sum([l * w for l, w in bertha])
    return agatha_area == bertha_area

