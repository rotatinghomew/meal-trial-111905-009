# 资料约定

原始资料均为本地合成。CSV 使用 UTF-8，首行是字段名。

所有重量用克。`trials` 记录同一餐段各窗口被分配的菜单、楼层及配给的备餐批，arm 是分配而非居民选择。`demand` 一行是一位到场者，wanted 是原选、served 是最终菜品，fulfilled 表示领餐，arrival 是分段分钟。requested_size 与 served_size 应分开；`refills` 是已发餐号的加餐，以克为单位。`weighings` 的 plate 限定到单餐、shared 只能定位到整个桶所列范围、unsold 是未售库存，记录不得重叠计算。`batches` 共享单位为克；`diversions` 是缺货窗口让居民去另一窗口的观测，不是发起第二份需求。`plans` 的 claimed_g 是经理已接受或拟接受的实际备餐量；applied 为已执行并不可撤回。`adjustments` 是称重新读数及记录日期。`policy` 定义组合对照的最少配对餐次和三项目标，以到场者为分母；abs_max_waste 是每人浪费克上限，min_original 和 min_fulfilled 是比例下限。
