#ifndef EXHAUSTIVE_SEARCH_ARCHIVE_HPP_
#define EXHAUSTIVE_SEARCH_ARCHIVE_HPP_

namespace limbo {
    namespace opt {
        template <typename Params>
        struct ExhaustiveSearchArchive {

            ExhaustiveSearchArchive() {}
            template <typename F>
            Eigen::VectorXd operator()(const F& f, const Eigen::VectorXd& init, bool bounded) const
            {
                float best_acqui = -INFINITY;
                Eigen::VectorXd result;

                typedef typename Params::archiveparams::archive_t::const_iterator archive_it_t;

                for (archive_it_t it = Params::archiveparams::archive.begin(); it != Params::archiveparams::archive.end(); ++it) {
                    Eigen::VectorXd temp(it->first.size());
                    for (size_t i = 0; i < it->first.size(); i++)
                        temp[i] = it->first[i];

                    float new_acqui = eval(f, temp);

                    if (best_acqui < new_acqui || it == Params::archiveparams::archive.begin()) {
                        best_acqui = new_acqui;
                        result = temp;
                    }
                }
                return result;
            }
        };
    }
}
#endif
