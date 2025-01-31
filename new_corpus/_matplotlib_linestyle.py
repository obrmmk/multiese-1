import matplotlib.pyplot as plt

データ列=[1,2,3]
データ列2=[2,3,4]

__X__='dashed'

linestyle = __X__
'''
@X('dashed';'dashbot';'dotted';'solid')
@Y(破線;一点鎖線;点線;実線)

＜オプション＞グラフの種類を__Y__に設定する
＜オプション＞[|グラフの]線種を__Y__に設定する
'''

plt.plot(データ列, データ列2, linestyle=__X__)
'''
{折れ線グラフ[のスタイル]を|__Y__に}設定する
__Y__[|の折れ線]グラフを描画する
{折れ線グラフを|__Y__で_}描画する
'''

plt.hist(データ列, linestyle=__X__)
'''
{ヒストグラム[の線のスタイル]を|__Y__に}設定する
__Y__ヒストグラムを描画する
{ヒストグラムを|__Y__で_}描画する
'''

