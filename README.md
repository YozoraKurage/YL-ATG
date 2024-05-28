# YozoLab-AbsoluteTransformGetter(YL-ATG)

YL-ATGはVRChatアバター上の任意のオブジェクトの絶対座標を取得するためのギミック/プログラムです。

まめひなたアイドルユニット「[ぱすてる](https://twitter.com/pastel_VRChat)」の動画撮影の為に作成しました。
主に[VRCPrismStudio](https://haruna.dev/prismstudio/)と併用することを目的としています。Thank you harunadev!!<3<3<3

## How-to-use

### **ATG_ForAvatar.unitypacage**は、アバターに組み込むためのパッケージです。
[ModulerAvatar](https://modular-avatar.nadena.dev/)を利用しています！事前にアバタープロジェクトへのインポートをお願いします。

1. ATG_ForAvatar.unitypacageをアバターのプロジェクトへインポートします。
2. Assets/YozoLab/YL-ATG_ForAvater/YL-ATG_ForAvatar.prefab をアバターの下に配置します。
3. ATG/pointのMA Bone Proxyにトラッキングしたいオブジェクトを指定してください。(デフォルトでHead)

これだけで導入は完了です！絶対座標を取得するには、専用のUnityプロジェクトを作成してください！
次に進みます↓

### **ATG_ForUnity.unitypacage**は、別のUnityプロジェクトに組み込み絶対座標を取得するパッケージです。
VRCPrismStudioとの併用を想定していますが、そうでなくても可能です。
OscCoreを利用します！付属の.unitypackageをインポートしてください。

**もし、PrismStudioのプロジェクトを既に作っている場合**
次の1. は不要です。

1. **UnityHub**で新たにプロジェクトを作成します(Recommend Unity 2022.3.6f1)
2. OscCore、ATG_ForUnityのUnityPackageをインポートします。
3. Assets/YozoLab/YL-ATG_ForUnity/SampleScenes にサンプルのプロジェクトがあるので、そのうちのどれかを開いてください。
4. PlayModeにすると同期が始まります。YL-ATG/TrackingObject のオブジェクトがVRCから取得した位置です！

## What is ATG_OSCHub?
Pythonを利用してOSCデータの分割を行うプログラムです！

ただし、処理が重いのでRustへの移行を検討に検討を重ね検討中です

撮影の為にカメラ位置を同期するため、TailScaleを利用して友人に座標を送り同期することを見据えたプログラムです。(ドキュメントに記述予定！)

~~pythonソースコードとexeを同梱しています。好きな方をお使いください！~~pyinstallerでビルドしたexeがWindowsセキュリティで抹消された；；

## Future Things
ちゃんとしたドキュメントを作成予定です！定期的にこのリポジトリをチェックするか、私の[~~X~~ Twitter](https://twitter.com/YozoraKurage)を見てください<3<3<3

## Varsions
2023/05/28-JST Ver0.0.1

## Use Libraries
- [OscCore](https://github.com/stella3d/OscCore)
- [python-osc](https://pypi.org/project/python-osc/)
 - pip3 install python-osc

## License
- [OscCore](https://github.com/stella3d/OscCore?tab=readme-ov-file#)

## Development Environment
Unity 2022.3.6f1

Python 3.10.14