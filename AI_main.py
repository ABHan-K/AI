import AI_Iteration as aii
import AI_Renumber_FloatToCoordinate as FtC

na = aii.Iteration('数据.xlsx')
ftc = FtC.Renumber_FloatToCoordinate('数据.xlsx')
result_DNA = na.main()
result_list = ftc.complete_node(result_DNA)
print(result_list)
