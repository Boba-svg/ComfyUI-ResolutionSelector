// File: web/index.js (ショートカット機能削除版)
// RESOLUTIONS, isInputFieldFocused, adjustResolution の定義は不要になりました。
// ノード名のみを定義します。

const NODE_NAME = "ResolutionSelector";

app.registerExtension({
    name: "ResolutionSelector",

    // setup() 関数を削除 (グローバルイベントリスナーが不要になったため)

    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === NODE_NAME) {
            // ノードの定義を調整する必要がなければ、この関数は空のままです
        }
    }
});
