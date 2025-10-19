# File: nodes.py (修正後)

class KeyControlResolution:
    # 固定の解像度リスト
    RESOLUTIONS = [384, 512, 640, 768, 896, 1024, 1152, 1280, 1408]
    
    # リストの最小間隔 (左右ボタン操作用)
    MIN_STEP = 128
    
    # ノードが属するカテゴリー: "utils"
    CATEGORY = "utils"
    
    # ノードの出力型と出力ポート名
    RETURN_TYPES = ("INT", "INT",)
    RETURN_NAMES = ("幅", "高さ",)
    
    FUNCTION = "execute"
    
    @classmethod
    def INPUT_TYPES(s):
        # ユーザーがノード上で値を設定するための入力ウィジェット
        return {
            "required": {
                "幅": ("INT", {
                    "default": 1024,
                    "min": min(s.RESOLUTIONS),
                    "max": max(s.RESOLUTIONS),
                    "step": s.MIN_STEP
                }),
                "高さ": ("INT", {
                    "default": 1024,
                    "min": min(s.RESOLUTIONS),
                    "max": max(s.RESOLUTIONS),
                    "step": s.MIN_STEP
                }),
            },
        }

    # ノードが実行されたときの処理
    def execute(self, 幅, 高さ):
        return (幅, 高さ,)

# ComfyUIにノードクラスを登録するためのマッピング
NODE_CLASS_MAPPINGS = {
    "ResolutionSelector": KeyControlResolution,
}

# ComfyUIのメニューに表示されるノード名
NODE_DISPLAY_NAME_MAPPINGS = {
    "ResolutionSelector": "解像度セレクター",
}

# 🚨 JavaScriptを読み込むために必要な定義 🚨
WEB_DIRECTORY = "web"