function [precision, recall, fmeasure] = evaluation_values(predicted, test, beta)
%EVALUATION_VALUES  calculate precision recall and f-measure
%  [precision, recall, fmeasure] = evaluation_values(predicted, test, beta)
%  beta is the weight of precision in the fmeasure use 1 as default

C = confusionmat(test, predicted);
precision = C(2,2)/(C(2,2)+C(1,2));
recall = C(2,2)/(C(2,2)+C(2,1));
fmeasure = (1+beta*beta)*recall*precision/(beta*beta*precision+recall);

end