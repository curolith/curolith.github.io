function newKey() {
    return Array(4).keys()
        .map(() => Array(4).keys()
            .map(Math.random).map(x => (x * 26) + 97).map(Math.floor)
            .map(x => String.fromCharCode(x)).toArray().join(""))
        .toArray().join("-")
}

const dataModelClassRegistry = {};

function register(classObject) {
    dataModelClassRegistry[classObject.className] = classObject;
    return classObject.className;
}

// Not persisted or rendered
class RuntimeData {
    static dataTypeKey = register(this);
    static children;
    static dataPrototype = {
    }
}

class TemplateData {
    static dataTypeKey = register(this);
    static dataPrototype = {
        dataType: TemplateData.dataTypeKey,
        children: [],
        // defines all keys with default values / value setters
    }
    static dataToHtml(data) {
        // visible data -> html
        // invisible data -> element.dataset.xyz = ...
        // mind the children
    }
    static htmlToData() {
        // inverse of data To Html
    }
    static HtmlToMarkdown() {
        // html ->  data -> markdown
    }
}

class RootData {
    static dataTypeKey = register(this);
    static dataPrototype = {
        dataType: RootData.dataTypeKey,
        children: [],
        configData: ConfigData.dataPrototype,
        bookData: BookData.dataPrototype
    }
    static dataToHtml(data) {
        // visible data -> html
        // invisible data -> element.dataset.xyz = ...
        // mind the children
    }
    static htmlToData() {
        // inverse of data To Html
    }
    static HtmlToMarkdown() {
        // html ->  data -> markdown
    }
}

class ConfigData {
    static dataTypeKey = register(this);
    static dataPrototype = {
        dataType: ConfigData.dataTypeKey,
        children: [],
        features: FeatureData.dataPrototype
    }
    static dataToHtml(data) {
        // visible data -> html
        // invisible data -> element.dataset.xyz = ...
        // mind the children
    }
    static htmlToData() {
        // inverse of data To Html
    }
    static HtmlToMarkdown() {
        // html ->  data -> markdown
    }
}

class FeatureData {
    static dataTypeKey = register(this);
    static dataPrototype = {
        dataType: FeatureData.dataTypeKey,
        syntaxHighlighting: false,
        autoSave: true
    }
    static dataToHtml(data) {
        // visible data -> html
        // invisible data -> element.dataset.xyz = ...
        // mind the children
    }
    static htmlToData() {
        // inverse of data To Html
    }
    static HtmlToMarkdown() {
        // html ->  data -> markdown
    }
}

class BookData {
    static dataTypeKey = register(this);
    static dataPrototype = {
        dataType: BookData.dataTypeKey,
        children: [],
    }
    static dataToHtml(data) {
        // visible data -> html
        // invisible data -> element.dataset.xyz = ...
        // mind the children
    }
    static htmlToData() {
        // inverse of data To Html
    }
    static HtmlToMarkdown() {
        // html ->  data -> markdown
    }
}

class CodeContentData {
    static dataTypeKey = register(this);
    static dataPrototype = {
        dataType: CodeContentData.dataTypeKey,
    }
    static dataToHtml(data) {
        // visible data -> html
        // invisible data -> element.dataset.xyz = ...
        // mind the children
    }
    static htmlToData() {
        // inverse of data To Html
    }
    static HtmlToMarkdown() {
        // html ->  data -> markdown
    }
}

class TextContentData {
    static dataTypeKey = register(this);
    static children;
    static dataPrototype = {
        dataType: TextContentData.dataTypeKey,
        htmlContent: "",
    }
    static dataToHtml(data) {
        // visible data -> html
        // invisible data -> element.dataset.xyz = ...
        // mind the children
    }
    static htmlToData() {
        // inverse of data To Html
    }
    static HtmlToMarkdown() {
        // html ->  data -> markdown
    }
}