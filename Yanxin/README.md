 ### 个人信息
 - 姓名：严薪
 - 邮箱：yan_xin@zju.edu.cn
 - 学号：21821130
 - 主题：复杂网络（ComplexNetworks）
 
 ### 选择论文
 
 [Complex Network Measures for Data Set Characterization](https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=6726419)
 
 * **Abstract**
 >This paper investigates the adoption of measures used to evaluate complex networks properties 
 in the characterization of the complexity of data sets in machine learning applications. These measures
 are obtained from a graph based representation of a data set. A graph representation has several 
 interesting properties as it can encode local neighborhood relations, as well as global characteristics
 of the data. These measures are evaluated in a meta-learning framework, where the objective is to predict
 which classifier will have better performance in a given task, in a pairwise basis comparison, based on 
 the complexity measures. Results were compared to traditional data set complexity characterization metrics,
 and shown the competitiveness of the proposed measures derived from the graph representation when compared
 to traditional complexity characterization metrics.
 
 * **摘要**
 >本文研究了复杂网络性能评估方法的应用。在描述机器学习应用中数据集的复杂性时。这些措施从基于图形的数据集表示中获得。图表示有几个有趣的属性，因为它可以编码局部邻域关系以及全局特征数据。这些指标在元学习框架中进行评估，其目标是预测哪一个分类器在给定的任务中，在成对的基础比较中具有更好的性能，基于复杂性度量。结果与传统的数据集复杂度表征指标进行了比较。并通过比较，展示了从图表示中得出的建议措施的竞争力。传统的复杂性特征度量。
 
 # 论文解读
 
>机器学习研究首先是一个实证研究领域，其目标是在给定的问题和合适的学习算法之间找到一个良好的匹配。这不是一项简单的任务，因为它是一种数据驱动的方法，并且有一些里程碑可以用来帮助指导为给定任务寻找合适的学习算法。这些地标通常基于领域特定的约束，例如生成模型的必要性或不可解释性以及部署或使用时间约束。此外，一般来说，对于要解决的给定问题，没有一种分析方法能够预先确定哪种算法是最佳的。因此，选择合适的算法来建立模型的方法通常需要一个经验的试错过程，这是一个成本高、耗时长的过程。解决这个问题的另一种方法是测量手头问题的某些特征，并利用这些特征来预测哪个算法在这个问题上会表现得很好，这是基于使用已知解的其他问题的特征（例如，经验确定的）建立的模型。这种方法被称为元学习，因为从参考问题集派生的元数据集中使用了一种监督学习算法来构建元类，以预测新问题的合适算法。为了构造元数据集，通常使用数据集的复杂性度量。这些度量被用作元数据集的元特征（或元特征）。这些复杂性度量是从数据集的矩阵数据表示中派生出来的。另一种表示数据集的方法是图形（或网络）表示，其中节点表示实例，边缘表示实例之间的关系。基于图的表示具有几个有趣的特性，因为它可以对边缘的局部邻域关系以及整个图中数据集的全局特征进行编码。本文研究了复杂网络理论的度量方法在数据集的图形表示中的应用，以构成元数据集的元特征。
 
 ### 传统的数据表征方法
 A.不同类别特征值重叠的度量  
 F1.最大Fisher判别比。此度量计算属性的最大识别能力（fisher比）。  
 F2.重叠区域的体积。这个度量计算由每个类的实例定义的分布尾部的重叠。  
 F3.最大的个性化功能效率。该度量计算单个特征的识别能力，并返回可以识别最大数量训练实例的属性值。  
 B.等级可分性度量  
 L1.最小误差距离之和。该方法评估训练数据在多大程度上是线性可分离的。线性可分离性是使用线性分类时正确分类的概率。对于两类问题，它对应于类在凸区域中分布时的重叠概率。  
 L2.线性规划的线性分类误差率。对于L1，这个度量提供了关于训练数据在多大程度上是线性可分离的信息。此度量是在训练集中测量的l1线性分类的错误率。
 N1.类边界上的点的分数。这个度量给出了类边界长度的估计。为此，在整个数据集上构建一个最小生成树，并返回将不同类的实例连接到同一类的生成树边缘的比率。该测量值较高表明，大多数点都靠近班级边界，因此，对于学习者来说，准确定义班级边界可能更为困难。
 N2.平均类内/类间最近邻距离之比。此度量将类内排列与其他类的最近邻距离进行比较。为此，对于每个实例，计算到同一类内和其各自类外最近邻居的距离。然后，计算到类间和类内最近邻的平均距离，并取它们之间的比率进行测量。这个度量的低值表明，同一类的示例紧密地位于特征空间中。高值表示同一类的例子是分散的。
 N3.一个最近邻类的错误率。该度量表示不同类的示例的接近程度。它返回一个最近邻居（k=1的knn类过滤器）学习者的漏掉一个错误率。这个度量的低值表示类边界中存在很大的间隙
