# TouhouMaps

这是 [zero318/TouhouMaps](https://github.com/zero318/TouhouMaps) 的维护分支。
`studio-ecl` 为 THTK-Studio 整理原生 thecl ECLM：共用版本与签名资料，
分别提供 zero318 和 Priw8 两套名称。上游根目录中的原始 map 保留原样。

## 使用

先加载共用定义，再加载一套名称。例如反编译 TH18：

```sh
thecl -d 18 -m common/th18.eclm -m names/zero318/th18.eclm input.ecl output.decl
thecl -d 18 -m common/th18.eclm -m names/priw8/th18.eclm input.ecl output.decl
```

编译时使用源码原先对应的名称方案：

```sh
thecl -c 18 -m common/th18.eclm -m names/priw8/th18.eclm input.decl output.ecl
```

切换名称方案会改变后续反编译输出的指令名和变量名，不会自动改写已有源码。
上述路径相对于调用目录；在别处运行时请传绝对路径。两份文件都以 `!eclmap`
开头，可直接通过 thecl 的多个 `-m` 参数加载，不需要转换器或运行时依赖。

## 资料范围

提供 Studio 当前支持的 22 个 ECL 版本的共用定义及两套名称配置：
TH06、07、08、09、095、10、103、11、12、125、128、13、14、143、15、16、
165、17、18、185、19、20。TH103 是黄昏酒场。体验版、TH06NC 和 ZECL
扩展不属于这批 stock 配置；它们已有的上游原始文件仍在根目录。

**这是可加载的资料基线，尚不是全部指令都已完成行为确认的集合。**

- `common/` 保存固定版本 thtk 的原生签名及全局变量类型。
- `names/zero318/`、`names/priw8/` 只保存指令、timeline 和变量名称。
- 优先保留该作品的上游名称。缺失风格的名称，仅在同一代 ECL、签名或类型
  一致且已有名称对应唯一时补入；这些条目注明 `fork correspondence`。
- 无可靠对应的条目保留 `unknown_123` / `unknown123` 等中性名称，注明
  `unresolved name`。没有把相邻作品的指令表直接认作本作的完整实现。

名称配置的风格标签包含本 fork 的补充条目，不表示两位上游作者已经提供或
确认全部作品。覆盖情况与待研究数量见 [覆盖表](docs/coverage.md)，逐条来源与
未解决的差异见 [初始归并记录](docs/import-audit.json)。

## 维护与验证

原生 `.eclm` 是维护对象。修改签名只改共用层，名称风格分别维护；新研究结果
按作品、命名空间及 opcode／变量 ID 记录来源。不要用字符串风格转换推断指令
语义，也不要直接将 truth 的扩展签名交给 thecl。

```sh
python3 scripts/validate.py
```

校验脚本只使用 Python 3 标准库，检查原生分段、两套名称覆盖、名称冲突和签名
基本语法，不下载或生成资料。实际完成的原生加载核对及其限制见
[验证记录](docs/validation.md)。

Studio 后续按固定 commit 引入这套资料，并统一编译、反编译、编辑器和 MCP
所用的版本与名称方案。本阶段没有修改 Studio 的配置或界面。

## 来源与许可

上游文件、原生签名和第三方名称的来源不同，详见 [SOURCES.md](SOURCES.md)。
根目录的 Unlicense 不自动覆盖第三方材料；thtk 的许可说明保存在 `licenses/`。
